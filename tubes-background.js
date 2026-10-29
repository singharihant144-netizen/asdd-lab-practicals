(() => {
  const canvas = document.querySelector(".tubes-canvas");
  const stage = canvas?.closest(".hero-art");
  const button = stage?.querySelector(".tube-colors");
  if (!canvas || !stage) return;
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduced) { stage.classList.add("tubes-static"); return; }
  let tubes;
  const randomPalette = count => Array.from({length: count}, () => `#${Math.floor(Math.random()*0xffffff).toString(16).padStart(6,"0")}`);
  const recolor = () => {
    if (!tubes?.tubes) return;
    tubes.tubes.setColors(randomPalette(3));
    tubes.tubes.setLightsColors(randomPalette(4));
  };
  button?.addEventListener("click", event => { event.stopPropagation(); recolor(); });
  stage.addEventListener("click", event => { if (!event.target.closest("button")) recolor(); });
  import("https://cdn.jsdelivr.net/npm/threejs-components@0.0.19/build/cursors/tubes1.min.js")
    .then(module => {
      if (!canvas.isConnected) return;
      const TubesCursor = module.default;
      tubes = TubesCursor(canvas, {tubes:{colors:["#9b6dff","#53e6c1","#ff4f9a"],lights:{intensity:160,colors:["#9b6dff","#53e6c1","#ff4f9a","#ffc857"]}}});
      stage.classList.add("tubes-ready");
    })
    .catch(() => { stage.classList.add("tubes-fallback"); const fallback=stage.querySelector(".tube-fallback"); if(fallback) fallback.hidden=false; });
})();
