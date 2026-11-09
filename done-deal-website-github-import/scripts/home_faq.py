from html import escape


QUESTIONS = (
    (
        'How does Done Deal work?',
        'Tell us what you want to drive, what you’d like to spend, and when you need it. We research options and negotiate with dealerships on your behalf. You review the offer and decide whether to move forward.',
    ),
    (
        'How much does it cost to work with Done Deal?',
        'Ask for a breakdown of any service fees, upfront costs, and monthly payments when you request a quote. Comparing the full cost helps you decide whether the deal makes sense for you.',
    ),
    (
        'I already have a dealer quote. Can you help?',
        'Yes. Share the offer and we can review the price, upfront costs, monthly payment, and terms. We’ll look for a better overall deal so you can compare your options side by side.',
    ),
    (
        'Can you help with my trade-in?',
        'Yes. Tell us what you’re driving now and share any trade-in offer you’ve already received. We’ll look at how the trade-in fits into the total cost of your next deal.',
    ),
    (
        'Can you help me get out of a lease early?',
        'We can help you explore your options. Whether it makes sense depends on your lease terms and any remaining payments or fees. Share your lease end date and mileage so we can start with the details.',
    ),
    (
        'Do you work with customers across the United States?',
        'We’ve helped customers from Virginia to California. Share your ZIP code and we’ll confirm what services are available in your area, including home delivery.',
    ),
    (
        'Do I need to know which car I want?',
        'No. Start with your budget and what matters most, like more room, a lower payment, or better fuel economy. We can help you narrow down the options.',
    ),
    (
        'Am I committing to anything by requesting a quote?',
        'No. It’s a conversation about your options, not a credit application or a commitment to buy or lease. You can review the details before deciding what to do next.',
    ),
)

FAQ_ICON = '<svg class="campaign-faq-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" aria-hidden="true" focusable="false"><path d="M5 12h14"/><path class="campaign-faq-plus" d="M12 5v14"/></svg>'


def render_home_faq():
    items = ''.join(
        f'<details class="campaign-faq-item"><summary>{FAQ_ICON}<span>{escape(question)}</span></summary>'
        f'<p>{escape(answer)}</p></details>'
        for question, answer in QUESTIONS
    )
    return f'''<section class="campaign-faq" id="faq" aria-labelledby="faq-heading"><div class="wrap">
 <div class="campaign-faq-heading"><h2 id="faq-heading">Frequently asked questions</h2><p>What to know before you buy, lease, or trade in with Done Deal.</p></div>
 <div class="campaign-faq-grid">{items}</div>
 <p class="campaign-faq-contact">Still have a question? <a class="text-link" href="/contact/">Talk to us</a></p>
</div></section>'''
