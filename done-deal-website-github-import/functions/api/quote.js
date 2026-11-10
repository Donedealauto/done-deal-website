const respond=(data,status=200)=>Response.json(data,{status,headers:{'Cache-Control':'no-store','X-Robots-Tag':'noindex'}});
export async function onRequestPost({request,env}) {
 if(!env.RESEND_API_KEY||!env.LEAD_TO_EMAIL||!env.LEAD_FROM_EMAIL||!env.TURNSTILE_SECRET_KEY)return respond({error:'Online sending is not available right now. Please use the email link on our contact page or call (631) 525-7010.'},503);
 if(request.headers.get('Origin')!==new URL(request.url).origin)return respond({error:'Please send your request from the Done Deal website.'},403);
 if(!request.headers.get('Content-Type')?.includes('application/json'))return respond({error:'Unsupported request format.'},415);
 if(Number(request.headers.get('Content-Length')||0)>16000)return respond({error:'Your request is too long.'},413);
 let data;try{const raw=await request.text();if(raw.length>16000)return respond({error:'Your request is too long.'},413);data=JSON.parse(raw);}catch{return respond({error:'Please check your request and try again.'},400);}
 if(!data||typeof data!=='object'||Array.isArray(data))return respond({error:'Invalid request.'},400);
 if(data.website)return respond({error:'Unable to process this request. Please contact Done Deal directly.'},400);
 const limits={name:100,email:254,phone:30,interest:100,vehicle:250,budget:100,timing:100,notes:2000,mileage:30,leaseEnd:7};
 for(const [key,max]of Object.entries(limits)){if(data[key]!=null&&(typeof data[key]!=='string'||data[key].length>max))return respond({error:'Please check the length of your form entries.'},400);data[key]=(data[key]||'').trim();}
 if(!data.name||!data.vehicle||!data.interest||!data.email||!/^\S+@[^\s@]+\.[^\s@]+$/.test(data.email)||/[\r\n]/.test(data.email)||data.consent!==true)return respond({error:'Please complete the required fields and contact agreement.'},400);
 if(!['Buy a new car','Lease a new car','Trade in a vehicle','Return a lease','Explore my options'].includes(data.interest))return respond({error:'Please select an inquiry type.'},400);
 if(typeof data.turnstileToken!=='string'||data.turnstileToken.length>3000)return respond({error:'Please complete the security check.'},400);
 try{
 const verification=await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify',{method:'POST',body:new URLSearchParams({secret:env.TURNSTILE_SECRET_KEY,response:data.turnstileToken}),signal:AbortSignal.timeout(10000)});
 if(!verification.ok)return respond({error:'The security check is unavailable. Please try again.'},503);
 const verified=await verification.json();if(!verified.success||verified.hostname!==new URL(request.url).hostname)return respond({error:'The security check expired. Please try again.'},400);
 const text=`New website inquiry\n\nName: ${data.name}\nEmail: ${data.email}\nPhone: ${data.phone||'Not provided'}\nInterest: ${data.interest}\nVehicle: ${data.vehicle}\nBudget: ${data.budget||'To discuss'}\nCurrent mileage: ${data.mileage||'Not provided'}\nLease end: ${data.leaseEnd||'Not provided'}\nTiming: ${data.timing||'Not specified'}\nNotes: ${data.notes||'None'}\n\nContact agreement: accepted\nReceived: ${new Date().toISOString()}`;
 const delivery=await fetch('https://api.resend.com/emails',{method:'POST',headers:{Authorization:`Bearer ${env.RESEND_API_KEY}`,'Content-Type':'application/json','Idempotency-Key':`quote-${await hash(data.turnstileToken)}`},body:JSON.stringify({from:env.LEAD_FROM_EMAIL,to:[env.LEAD_TO_EMAIL],reply_to:data.email,subject:'New Done Deal website inquiry',text}),signal:AbortSignal.timeout(15000)});
 if(!delivery.ok)return respond({error:'We couldn’t send your request. Please try again, or call (631) 525-7010.'},502);
 return respond({ok:true});
 }catch{return respond({error:'We couldn’t confirm delivery. Please contact Done Deal at (631) 525-7010.'},502);}
}
async function hash(value){const bytes=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(value));return Array.from(new Uint8Array(bytes),b=>b.toString(16).padStart(2,'0')).join('');}
export function onRequest(){return respond({error:'Method not allowed.'},405);}
