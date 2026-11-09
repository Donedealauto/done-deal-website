(() => {
 const video = document.querySelector('[data-road-video]');
 const control = document.querySelector('[data-road-control]');
 if (!video || !control) return;

 const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
 const connection = navigator.connection;
 let pausedByVisitor = false;

 function syncControl() {
  const playing = !video.paused;
  control.toggleAttribute('data-playing', playing);
  control.setAttribute('aria-label', playing ? 'Pause background video' : 'Play background video');
 }

 function play() {
  video.play().catch(syncControl);
 }

 function syncMotion() {
  if (motion.matches || connection?.saveData) {
   video.pause();
   control.hidden = true;
   return;
  }
  if (!video.getAttribute('src')) video.src = video.dataset.src;
  control.hidden = Boolean(video.error);
  if (!pausedByVisitor && !video.error) play();
 }

 video.addEventListener('play', syncControl);
 video.addEventListener('pause', syncControl);
 video.addEventListener('error', () => { control.hidden = true; });
 control.addEventListener('click', () => {
  pausedByVisitor = !video.paused;
  if (pausedByVisitor) video.pause();
  else play();
 });
 motion.addEventListener('change', syncMotion);
 connection?.addEventListener('change', syncMotion);
 syncMotion();
})();
