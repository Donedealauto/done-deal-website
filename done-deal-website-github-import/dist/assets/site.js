const toggle=document.querySelector('.menu-toggle');
const nav=document.querySelector('#navigation');
toggle?.addEventListener('click',()=>{const expanded=toggle.getAttribute('aria-expanded')==='true';toggle.setAttribute('aria-expanded',String(!expanded));nav.classList.toggle('open',!expanded);toggle.setAttribute('aria-label',expanded?'Open menu':'Close menu');if(!expanded)nav.querySelector('a')?.focus({preventScroll:true});});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav?.classList.contains('open')){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-label','Open menu');toggle.focus();}});
const form=document.querySelector('#quote-form');
if(form){
 const recipient=form.querySelector('.request-recipient a').getAttribute('href').slice('mailto:'.length);
 const status=document.querySelector('#form-status'), submit=document.querySelector('#submit-quote');
 const review=document.querySelector('#email-actions'), preview=document.querySelector('#request-preview');
 const heading=document.querySelector('#delivery-heading'), note=document.querySelector('#delivery-note');
 let configured=false, token='', requestText='', busy=false, prepared=false;
 const announce=message=>{status.textContent=message;};
 const errors=document.querySelector('#form-errors');
 const controls=[...form.querySelectorAll('input:not([name="website"]),select,textarea:not([readonly])')];
 const invalidMessage=field=>{
  if(field.disabled)return '';
  if(field.required&&(field.type==='checkbox'?!field.checked:!field.value.trim()))return field.name==='consent'?'Please agree to be contacted about this request.':({name:'Enter your name.',email:'Enter your email address.',interest:'Choose what you’d like help with.',vehicle:'Tell us about the vehicle, or write “Not sure yet.”'}[field.name]||'Complete this field.');
  if(field.validity.typeMismatch)return 'Enter a valid email address, such as you@example.com.';
  if(!field.validity.valid)return 'Please check this entry.';
  return '';
 };
 const showError=field=>{
  const message=invalidMessage(field),error=document.getElementById(field.id+'-error');
  error.textContent=message;error.hidden=!message;
  if(message)field.setAttribute('aria-invalid','true');else field.removeAttribute('aria-invalid');
  return message;
 };
 controls.forEach(field=>{
  field.id=field.id||'quote-'+field.name;
  const error=document.createElement('small');error.id=field.id+'-error';error.className='field-error';error.hidden=true;
  field.closest('label').append(error);
  field.setAttribute('aria-describedby',[field.getAttribute('aria-describedby'),error.id].filter(Boolean).join(' '));
  field.addEventListener('blur',()=>{if(field.value||field.getAttribute('aria-invalid'))showError(field);});
 });
 form.noValidate=true;
 const updateIntent=()=>{
  const interest=form.elements.interest.value, current=['Trade in a vehicle','Return a lease'].includes(interest), leasing=interest==='Lease a new car';
  document.querySelector('#vehicle-label').textContent=current?'Your current vehicle *':'Vehicle preferences *';
  form.elements.vehicle.placeholder=current?'Year, make and model':'Make, model, or what matters most';
  document.querySelector('#vehicle-hint').textContent=current?'Tell us which vehicle you have. An approximate year or model is fine.':'Still deciding? Tell us what matters most, or write “Not sure yet.”';
  document.querySelector('#budget-label').textContent=leasing?'Monthly budget + upfront amount (optional)':'Total vehicle budget (optional)';
  form.elements.budget.placeholder=leasing?'e.g. $450/month, $2,000 upfront':'e.g. $35,000, or to discuss';
  document.querySelector('#budget-field').hidden=current;form.elements.budget.disabled=current;
  form.querySelectorAll('[data-interests]').forEach(label=>{const visible=label.dataset.interests.split('|').includes(interest);label.hidden=!visible;label.querySelectorAll('input').forEach(input=>{input.disabled=!visible;if(!visible)showError(input);});});
 };
 form.elements.interest.addEventListener('change',updateIntent);updateIntent();
 const validate=()=>{
  errors.replaceChildren();const invalid=controls.filter(field=>showError(field));
  errors.hidden=!invalid.length;if(!invalid.length)return true;
  const title=document.createElement('p');title.textContent='Please check '+invalid.length+(invalid.length===1?' field':' fields')+' before continuing.';errors.append(title);
  const list=document.createElement('ul');invalid.forEach(field=>{const item=document.createElement('li'),link=document.createElement('a');link.href='#'+field.id;link.textContent=invalidMessage(field);link.addEventListener('click',e=>{e.preventDefault();field.focus();});item.append(link);list.append(item);});errors.append(list);errors.focus();return false;
 };
 const requestData=()=>({...Object.fromEntries([...new FormData(form)].map(([key,value])=>[key,typeof value==='string'?value.trim():value])),consent:form.elements.consent.checked});
 const prepare=(data,uncertain=false)=>{
  requestText=`Done Deal quote request\n\nName: ${data.name}\nEmail: ${data.email}\nPhone: ${data.phone||'Not provided'}\nLooking to: ${data.interest}\nVehicle: ${data.vehicle}${data.budget?'\nBudget: '+data.budget:''}${data.mileage?'\nCurrent mileage: '+data.mileage:''}${data.leaseEnd?'\nLease end: '+data.leaseEnd:''}\nTiming: ${data.timing}\nNotes: ${data.notes||'None'}\n\nI agree to be contacted about this request.`;
  preview.value=requestText;
  document.querySelector('#email-link').href=`mailto:${recipient}?subject=${encodeURIComponent('Vehicle inquiry — '+data.name)}&body=${encodeURIComponent(requestText)}`;
  document.querySelector('#request-send-note').textContent=uncertain?'Online delivery could not be confirmed. You can email this copy instead, or call Done Deal to check before sending again.':'Your request has not been sent. Open your email app, check the message, then press Send.';
  review.hidden=false;prepared=true;
  document.querySelector('#request-review-heading').focus();
 };
 fetch('/api/config',{headers:{Accept:'application/json'},signal:AbortSignal.timeout(5000)}).then(async r=>{
  if(!r.ok||!r.headers.get('content-type')?.includes('application/json'))return;
  const c=await r.json();if(c.enabled!==true||typeof c.turnstileSiteKey!=='string'||!c.turnstileSiteKey)return;
  window.onDoneDealTurnstile=()=>{
   if(prepared||!window.turnstile)return;
   try{
    window.turnstile.render('#turnstile',{sitekey:c.turnstileSiteKey,callback:t=>{token=t;},'expired-callback':()=>{token='';announce('The security check expired. Please complete it again before sending.');},'error-callback':()=>{token='';announce('The security check is unavailable. Try again, or call (631) 525-7010.');}});
    configured=true;submit.textContent='Send my request';heading.textContent='Send your request to Done Deal';note.textContent='Your inquiry will be sent directly to Done Deal. We’ll confirm here when it has been accepted for delivery.';
   }catch{configured=false;}
  };
  const script=document.createElement('script');script.src='https://challenges.cloudflare.com/turnstile/v0/api.js?onload=onDoneDealTurnstile&render=explicit';script.async=true;document.head.append(script);
 }).catch(()=>{});
 form.addEventListener('input',e=>{if(e.target===preview)return;if(e.target.getAttribute('aria-invalid'))showError(e.target);errors.hidden=true;if(!review.hidden){review.hidden=true;announce('Your details changed. Prepare your request again to update the message.');}requestText='';});
 form.addEventListener('submit',async e=>{
  e.preventDefault();if(busy||!validate())return;
  const data=requestData();if(data.website)return;
  announce('');review.hidden=true;
  if(!configured){prepare(data);announce('Request prepared—not sent. Review it below and send it from your email app.');return;}
  if(!token){prepare(data);announce('Please complete the security check to send online, or use the email option below.');return;}
  busy=true;submit.disabled=true;submit.textContent='Sending…';controls.forEach(field=>{field.dataset.wasDisabled=String(field.disabled);field.disabled=true;});
  try{
   const r=await fetch('/api/quote',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({...data,turnstileToken:token}),signal:AbortSignal.timeout(30000)});
   const result=r.headers.get('content-type')?.includes('application/json')?await r.json():null;
   if(!r.ok||result?.ok!==true){const error=new Error('delivery-unconfirmed');error.status=r.status;throw error;}
   announce('Thank you. Your request has been accepted for delivery to Done Deal. We’ll follow up using the details you provided.');form.reset();controls.forEach(field=>{field.removeAttribute('aria-invalid');document.getElementById(field.id+'-error').hidden=true;});
  }catch(error){
   prepare(data,true);announce(error.status===429?'Too many attempts. Please wait a few minutes before trying again, or use the email option below.':error.status===400?'We couldn’t accept the request. Check your details and complete a fresh security check, or use the email option below.':'We couldn’t confirm online delivery. Your details are still here. Review the email option below, or call (631) 525-7010.');
  }finally{controls.forEach(field=>{field.disabled=field.dataset.wasDisabled==='true';});updateIntent();busy=false;submit.disabled=false;submit.textContent='Send my request';token='';window.turnstile?.reset();}
 });
 document.querySelector('#copy-request').addEventListener('click',async()=>{
  try{await navigator.clipboard.writeText(requestText);announce('Message copied. Paste it into an email to '+recipient+' and press Send. Copying does not send it.');}
  catch{preview.focus();preview.select();announce('Automatic copying is unavailable. The message is selected—copy it manually, then paste it into your email.');}
 });
 document.querySelector('#edit-request').addEventListener('click',()=>{review.hidden=true;announce('Update your details, then prepare your request again.');form.elements.name.focus();});
}
