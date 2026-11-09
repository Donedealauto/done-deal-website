document.querySelectorAll('[data-stories]').forEach(section => {
 const track = section.querySelector('.stories-track');
 const cards = [...track.children];
 const controls = section.querySelector('.stories-controls');
 const arrows = [...controls.querySelectorAll('[data-story-step]')];
 const dots = [...controls.querySelectorAll('[data-story-go]')];
 const status = section.querySelector('.story-status');
 const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
 if (cards.length < 2) return;
 let active = -1, pending = null, frame = 0;
 const offset = card => card.offsetLeft - cards[0].offsetLeft;
 const update = () => {
  frame = 0;
  const closest = cards.reduce((best, card, i) =>
   Math.abs(offset(card) - track.scrollLeft) < Math.abs(offset(cards[best]) - track.scrollLeft) ? i : best, 0);
  if (pending !== null && Math.abs(offset(cards[pending]) - track.scrollLeft) < 2) pending = null;
  if (closest === active) return;
  const initial = active === -1;
  active = closest;
  dots.forEach((dot, i) => i === active ? dot.setAttribute('aria-current', 'true') : dot.removeAttribute('aria-current'));
  arrows.forEach((arrow, i) => arrow.setAttribute('aria-disabled', String(i === 0 ? active === 0 : active === cards.length - 1)));
  if (!initial) status.textContent = cards[active].getAttribute('aria-label');
 };
 const go = index => {
  if (index < 0 || index >= cards.length) return;
  pending = index;
  track.scrollTo({ left: offset(cards[index]), behavior: reduceMotion.matches ? 'instant' : 'smooth' });
 };
 const move = step => go((pending ?? active) + step);
 section.classList.add('is-slider');
 track.tabIndex = 0;
 track.setAttribute('role', 'group');
 track.setAttribute('aria-label', 'Customer stories. Use left and right arrows to browse.');
 controls.hidden = false;
 update();
 track.addEventListener('scroll', () => { if (!frame) frame = requestAnimationFrame(update); }, { passive: true });
 track.addEventListener('pointerdown', () => { pending = null; }, { passive: true });
 track.addEventListener('wheel', event => { if (event.deltaX || event.shiftKey) pending = null; }, { passive: true });
 arrows.forEach(arrow => arrow.addEventListener('click', () => move(Number(arrow.dataset.storyStep))));
 dots.forEach(dot => dot.addEventListener('click', () => go(Number(dot.dataset.storyGo))));
 section.addEventListener('keydown', event => {
  if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey || !['ArrowLeft', 'ArrowRight'].includes(event.key)) return;
  event.preventDefault();
  move(event.key === 'ArrowLeft' ? -1 : 1);
 });
});
