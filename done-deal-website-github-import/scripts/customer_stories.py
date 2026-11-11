from road_hero import render_road_hero
"""Customer story data and renderers for the homepage and story index."""
from html import escape

STORIES = (
    {
        'name': 'Ed', 'location': 'Virginia', 'slug': 'virginia',
        'image': 'ed-sienna.webp', 'size': (1440, 1126),
        'alt': 'Ed standing beside his silver Toyota Sienna',
        'title': 'A roomier ride, delivered to his driveway.',
        'summary': 'Ed ended his lease early and moved into a Toyota Sienna. We delivered his new car to his Virginia home and picked up the old one on the same visit.',
    },
    {
        'name': 'Liz', 'location': 'Long Island, NY', 'slug': 'liz',
        'image': 'liz-mdx.webp', 'size': (1080, 1440),
        'alt': 'Liz beside her Acura MDX, with the license plate blurred',
        'title': 'A fresh start in a new Acura MDX.',
        'summary': 'With more than 100,000 miles on her old car, Liz was ready for an upgrade. Done Deal matched another dealership’s trade-in offer and helped her lease a new Acura MDX.',
    },
    {
        'name': 'Joanne', 'location': 'Long Island, NY', 'slug': 'joanne',
        'image': 'joanne-car.webp', 'size': (1080, 1440),
        'alt': 'Joanne beside her new car, with the license plate blurred',
        'title': 'A better price and days of shopping saved.',
        'summary': 'Joanne had already visited several dealerships and compared quotes. Done Deal took over the search, found her a better deal, and saved her days of additional research.',
    },
    {
        'name': 'Christina', 'location': 'California', 'slug': 'california',
        'image': 'christina-mercedes.webp', 'size': (1080, 1440),
        'alt': 'Christina waving from the driver’s seat of her white Mercedes-Benz GLS 450',
        'title': 'Thousands saved on a new Mercedes.',
        'summary': 'Christina saved thousands on her 2026 Mercedes-Benz GLS 450 compared to her dealership quote. She also ended her existing lease early with no additional charges.',
    },
)

def render_stories(show_index_link=False):
    cards, dots = [], []
    count = len(STORIES)
    for i, story in enumerate(STORIES, 1):
        name, location, slug, title, summary = (
            escape(story[key]) for key in ('name', 'location', 'slug', 'title', 'summary')
        )
        image, alt = escape(story['image'], quote=True), escape(story['alt'], quote=True)
        width, height = story['size']
        meta = f'{name} <span aria-hidden="true">·</span> {location}' if location else name
        cards.append(f'''<article class="story-slide" data-story="{slug}" aria-label="Story {i} of {count}: {name}">
 <div class="story-slide-art"><img src="/assets/{image}" width="{width}" height="{height}" alt="{alt}" loading="lazy"></div>
 <div class="story-slide-copy"><p class="story-slide-meta">{meta}</p><h3>{title}</h3><p class="story-slide-summary">{summary}</p><a class="story-slide-link" href="/customer-stories/{slug}/">Read {name}’s story <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M6 18 18 6M8 6h10v10"/></svg></a></div>
</article>''')
        dots.append(f'<button type="button" class="story-dot" data-story-go="{i-1}" aria-label="Show {name}’s story"></button>')
    index_link = '<a class="stories-view-all" href="/customer-stories/">View All Testimonials <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 12h15m-6-6 6 6-6 6"/></svg></a>' if show_index_link else ''
    return f'''<section class="stories-carousel" aria-labelledby="proof-heading" data-stories>
 <div class="wrap stories-carousel-heading">
  <h2 id="proof-heading">Real customers. Better deals.</h2>
  <p class="stories-carousel-lead">No two deals are the same. Whether you’re trading in, ending a lease early, or looking for a better price, we help you find what works for you.</p>
  {index_link}
 </div>
 <div class="stories-track" id="stories-track">{''.join(cards)}</div>
 <div class="stories-carousel-footer wrap">
  <div class="stories-controls" role="group" aria-label="Customer story controls" hidden>
   <button type="button" class="story-arrow" data-story-step="-1" aria-label="Previous story" aria-controls="stories-track"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M20 12H4m7-7-7 7 7 7"/></svg></button>
   <div class="story-dots">{''.join(dots)}</div>
   <button type="button" class="story-arrow" data-story-step="1" aria-label="Next story" aria-controls="stories-track"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M4 12h16m-7-7 7 7-7 7"/></svg></button>
  </div>
  <span class="story-status" aria-live="polite" aria-atomic="true"></span>
 </div>
</section>'''


STORY_TOPICS = {
    'virginia': 'Early lease exit · Home delivery',
    'liz': 'Trade-in · New lease',
    'joanne': 'Price comparison · Time saved',
    'california': 'Lease savings · Early exit',
}


def render_story_index():
    rows = []
    for i, story in enumerate(STORIES, 1):
        name, location, slug, title, summary, image, alt = (
            escape(story[key], quote=True)
            for key in ('name', 'location', 'slug', 'title', 'summary', 'image', 'alt')
        )
        topic = escape(STORY_TOPICS[story['slug']])
        width, height = story['size']
        loading = 'eager' if i == 1 else 'lazy'
        rows.append(f'''<article class="story-index-row" data-story="{slug}" aria-labelledby="story-title-{slug}">
 <div class="wrap story-index-layout">
  <div class="story-index-photo"><img src="/assets/{image}" width="{width}" height="{height}" loading="{loading}" alt="{alt}"></div>
  <div class="story-index-copy">
   <p class="story-index-meta">{name} <span aria-hidden="true">·</span> {location}</p>
   <h2 id="story-title-{slug}">{title}</h2>
   <p class="story-index-summary">{summary}</p>
   <p class="story-index-topic">{topic}</p>
   <a class="story-index-link" href="/customer-stories/{slug}/">Read {name}’s story <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 12h15m-6-6 6 6-6 6"/></svg></a>
  </div>
 </div>
</article>''')
    hero = render_road_hero(
        'Testimonials',
        'Every deal<br>has a story.',
        'See how Done Deal helped four customers find a better price, make an easier switch, or get their time back.',
        'stories-open-road',
        heading_id='proof-heading',
    )
    return f'{hero}<div class="story-index-list">{"".join(rows)}</div>'
