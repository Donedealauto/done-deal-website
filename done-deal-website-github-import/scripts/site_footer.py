from html import escape


ICON_PATHS = {
    'arrow': '<path d="M4 12h15m-6-6 6 6-6 6"/>',
    'phone': '<path d="m8 3 2 4-2.5 2.5a15 15 0 0 0 7 7L17 14l4 2v3a2 2 0 0 1-2.2 2A19.5 19.5 0 0 1 3 5.2 2 2 0 0 1 5 3z"/>',
    'text': '<path d="M5 4h14a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H9l-5 4v-4a2 2 0 0 1-1-2V6a2 2 0 0 1 2-2zM8 9h8m-8 4h5"/>',
    'email': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m4 7 8 6 8-6"/>',
    'instagram': '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".7" fill="currentColor" stroke="none"/>',
    'pin': '<path d="M19 10c0 5-7 10-7 10S5 15 5 10a7 7 0 1 1 14 0z"/><circle cx="12" cy="10" r="2.25"/>',
}


def icon(name):
    return f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{ICON_PATHS[name]}</svg>'


def render_footer(nav):
    links = ''.join(f'<li><a href="{escape(url, quote=True)}">{escape(label)}</a></li>' for url, label in nav if url != '/')
    return f'''<footer class="site-footer" id="site-footer">
 <div class="wrap site-footer-inner">
  <div class="site-footer-intro">
   <a class="site-footer-logo" href="/" aria-label="Done Deal Auto Group home"><img src="/assets/logo.png" width="574" height="490" alt="" loading="lazy"></a>
   <p class="site-footer-line">A better deal.<br><span>Already handled.</span></p>
  </div>
  <div class="site-footer-links">
   <div role="navigation" aria-label="Footer navigation">
    <h2>Explore</h2>
    <ul class="site-footer-nav">{links}</ul>
   </div>
   <div>
    <h2>Let’s talk</h2>
    <ul class="site-footer-contact">
     <li><a href="tel:+16315257010"><span class="site-footer-icon">{icon('phone')}</span><span>(631) 525-7010</span></a></li>
     <li><a href="sms:+16315257010"><span class="site-footer-icon">{icon('text')}</span><span>Send a text</span></a></li>
     <li><a href="mailto:info@donedealautogroup.com"><span class="site-footer-icon">{icon('email')}</span><span>Email Done Deal</span></a></li>
     <li><a href="https://www.instagram.com/donedealautogroup/" aria-label="@donedealautogroup on Instagram"><span class="site-footer-icon">{icon('instagram')}</span><span>@donedealautogroup</span></a></li>
    </ul>
   </div>
   <div>
    <h2>Find us</h2>
    <address class="site-footer-location"><span class="site-footer-icon">{icon('pin')}</span><span>10 Burt Drive<br>Deer Park, NY 11729</span></address>
    <a class="site-footer-cta" href="/request-a-quote/">Request a quote {icon('arrow')}</a>
   </div>
  </div>
  <div class="site-footer-credits"><span>© 2026 Done Deal Auto Broker Inc.</span><span>Website by KB Media</span></div>
 </div>
</footer>'''
