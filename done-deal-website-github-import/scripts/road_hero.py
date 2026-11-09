"""Shared video hero for the main interior pages."""

from html import escape


def render_road_hero(page, title, description, clip, heading_id="page-heading"):
    poster = f"/assets/{clip}.webp"
    return f'''<section class="road-hero" aria-labelledby="{heading_id}" style="--road-poster: url('{poster}')">
 <video class="road-hero-video" data-road-video data-src="/assets/{clip}.mp4" poster="{poster}" preload="none" muted loop playsinline aria-hidden="true"></video>
 <div class="wrap road-hero-intro">
  <p class="road-hero-kicker">{escape(page)}</p>
  <h1 id="{heading_id}">{title}</h1>
  <p class="road-hero-lead">{escape(description)}</p>
 </div>
 <button class="road-hero-control" type="button" data-road-control aria-label="Play background video" hidden>
  <svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false">
   <path class="road-icon-play" d="M8 5.5a.75.75 0 0 0-1.15.63v11.74a.75.75 0 0 0 1.15.63l9.5-5.87a.75.75 0 0 0 0-1.26z"/>
   <path class="road-icon-pause" d="M7 5h3a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm7 0h3a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1h-3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1z"/>
  </svg>
 </button>
</section>'''
