from customer_stories import render_stories
from home_faq import render_home_faq

INTENT_ARROW = '<svg class="campaign-intent-arrow" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4.5 12h14m-5.5-5.5 5.5 5.5-5.5 5.5"/></svg>'


def render_home():
 return '''
<section class="campaign-hero wrap" aria-labelledby="hero-heading">

 <div class="campaign-opening">
  <h1 id="hero-heading">Car shopping sucks.<br><span>We do it for you.</span></h1>
  <div class="campaign-intro"><p>Your next car. Hassle free. From the comfort of your home.</p><div class="actions"><a class="button" href="/request-a-quote/">Request a quote</a><a class="button campaign-call campaign-contact-desktop" href="/contact/">Talk to us</a><a class="button campaign-call campaign-contact-mobile" href="tel:+16315257010">Talk to us</a></div></div>
 </div>
 <div class="campaign-panorama"><img src="/assets/family-handoff-pulled-back.webp" srcset="/assets/family-handoff-mobile.webp 768w, /assets/family-handoff-pulled-back.webp 1000w" sizes="(max-width: 760px) calc(88vw - 35px), (max-width: 1330px) 42vw, 550px" width="1000" height="1000" fetchpriority="high" alt="Illustrative family receiving the keys beside a new Volvo SUV in a driveway"></div>
</section>
<section class="campaign-value" id="why-done-deal" aria-labelledby="value-heading"><div class="wrap">
 <div class="campaign-value-heading"><h2 id="value-heading">Why choose Done Deal?</h2><p>Your time back. A better deal.<br> A clear path to your next car.</p></div>
 <div class="campaign-benefits">
  <article class="campaign-benefit benefit-time"><div class="benefit-copy"><h3>Your weekends. Back.</h3><p>Skip the dealership visits and hours on the phone haggling. We handle the search and negotiations. You spend your time on what matters.</p></div><img src="/assets/benefit-weekend-couple.webp" width="1400" height="1050" loading="lazy" alt="Illustrative senior couple enjoying a relaxed weekend by the harbor"></article>
  <article class="campaign-benefit benefit-savings"><img src="/assets/benefit-city-driver.webp" width="1400" height="1050" loading="lazy" alt="Illustrative driver behind the wheel of a premium sedan on a city street"><div class="benefit-copy"><h3>Around 10% less. Every month.</h3><p>Our negotiators typically save customers around 10% on their monthly lease payment. A better deal, without doing the back-and-forth yourself.</p><p class="benefit-note">Typical savings; individual results vary.</p></div></article>
  <article class="campaign-benefit benefit-clarity"><div class="benefit-copy"><h3>Clear answers. Confident decisions.</h3><p>Price, payments, upfront costs and terms—explained clearly. We answer your questions so you understand the deal before you decide.</p></div><img src="/assets/benefit-clear-options.webp" width="1400" height="1050" loading="lazy" alt="Illustrative Asian couple reviewing vehicle options with an advisor"></article>
 </div>
 <div class="campaign-value-action"><a class="campaign-value-link" href="/services/">See how Done Deal helps <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 12h15m-6-6 6 6-6 6"/></svg></a></div>
</div></section>
''' + render_stories(show_index_link=True) + '''
<section class="campaign-process" aria-labelledby="process-heading"><div class="wrap"><h2 id="process-heading">From wishlist to driveway.</h2><p class="campaign-process-intro">You tell us what you want. We take it from there.</p><ol><li><span aria-hidden="true">01</span><h3>Tell us what matters.</h3><p>Your vehicle, budget and timing.</p></li><li><span aria-hidden="true">02</span><h3>We do the legwork.</h3><p>We explore your options and negotiate the deal.</p></li><li><span aria-hidden="true">03</span><h3>You make the call.</h3><p>Review the offer and decide what’s right for you.</p></li></ol></div></section>
<section class="campaign-close" aria-labelledby="quote-heading"><div class="wrap"><h2 id="quote-heading">Ready for a better deal?</h2><a class="button" href="/request-a-quote/">Request a quote</a></div></section>
''' + render_home_faq() + '''
<section class="campaign-intents" aria-labelledby="intent-heading"><div class="wrap"><h2 id="intent-heading">What’s your next move?</h2><div class="campaign-intent-links"><a href="/request-a-quote/?interest=buy"><span class="campaign-intent-label">Buy a new car</span> ''' + INTENT_ARROW + '''</a><a href="/request-a-quote/?interest=lease"><span class="campaign-intent-label">Lease a new car</span> ''' + INTENT_ARROW + '''</a><a href="/request-a-quote/?interest=trade"><span class="campaign-intent-label">Trade in a vehicle</span> ''' + INTENT_ARROW + '''</a><a href="/request-a-quote/?interest=return"><span class="campaign-intent-label">Return a lease</span> ''' + INTENT_ARROW + '''</a></div></div></section>
'''
