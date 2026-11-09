(() => {
 const header=document.querySelector('header');
 let pending=false;
 const update=()=>{pending=false;header?.classList.toggle('is-scrolled',scrollY>8);};
 window.addEventListener('scroll',()=>{if(!pending){pending=true;requestAnimationFrame(update);}},{passive:true});update();
 // Motion supports the content. There are no pinned scenes or extra scroll spans.
 if(window.ScrollCraft){
  document.querySelectorAll('.value-ledger article,.dd-story,.dd-steps li,.interior-page .page-intro,.interior-page .contact-card').forEach(el=>el.setAttribute('data-sc-in',''));
  window.ScrollCraft.mount(document);
 }
 const form=document.querySelector('#quote-form');
 if(form){const values={buy:'Buy a new car',lease:'Lease a new car',trade:'Trade in a vehicle',return:'Return a lease'};const interest=new URLSearchParams(location.search).get('interest');if(values[interest]){form.elements.interest.value=values[interest];form.elements.interest.dispatchEvent(new Event('change',{bubbles:true}));}}
})();
