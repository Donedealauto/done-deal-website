export function onRequestGet({env}) {
 const enabled=Boolean(env.RESEND_API_KEY&&env.LEAD_TO_EMAIL&&env.LEAD_FROM_EMAIL&&env.TURNSTILE_SECRET_KEY&&env.TURNSTILE_SITE_KEY);
 return Response.json({enabled,turnstileSiteKey:enabled?env.TURNSTILE_SITE_KEY:null},{headers:{'Cache-Control':'no-store'}});
}
