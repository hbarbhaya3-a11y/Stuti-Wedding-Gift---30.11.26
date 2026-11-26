const C = Object.assign({ you: "[Your Name]", partner: "[Partner Name]", day: "00", month: "Month", year: "2027" }, window.MAG_CONFIG || {});
const fills = {
  you: C.you, partner: C.partner, day: C.day, year: C.year,
  monthYear: (C.month + " " + C.year).toUpperCase(),
  couple: C.you + " & " + C.partner,
  coupleCaps: (C.you + " & " + C.partner).toUpperCase(),
  dateLong: C.day + " " + C.month + " " + C.year
};
document.querySelectorAll("[data-fill]").forEach(el => { if (fills[el.dataset.fill] != null) el.textContent = fills[el.dataset.fill]; });
document.querySelectorAll(".ph[data-src]").forEach(el => {
  const img = new Image();
  img.onload = () => { el.style.backgroundImage = `url("${el.dataset.src}")`; el.classList.add("loaded"); };
  img.src = el.dataset.src;
});
const pages = [...document.querySelectorAll(".page")];
pages.forEach((p, i) => { if (i > 0 && i < pages.length - 1) { const n = document.createElement("div"); n.className = "pageno"; n.textContent = String(i + 1).padStart(2, "0"); p.appendChild(n); } });
const book = document.getElementById("book");
let views = [], v = 0;
function buildViews() {
  const single = window.innerWidth < 900 || window.innerHeight > window.innerWidth;
  book.classList.toggle("single", single);
  if (single) views = pages.map((_, i) => [i]);
  else { views = [[0]]; for (let i = 1; i < pages.length - 1; i += 2) views.push(i + 1 < pages.length - 1 ? [i, i + 1] : [i]); views.push([pages.length - 1]); }
}
function render() {
  pages.forEach(p => p.classList.remove("show", "left", "right"));
  const cur = views[v];
  cur.forEach((i, k) => { pages[i].classList.add("show"); if (cur.length === 2) pages[i].classList.add(k ? "right" : "left"); });
  document.getElementById("count").textContent = cur.map(i => i + 1).join("–") + " / " + pages.length;
  document.getElementById("prev").disabled = v === 0;
  document.getElementById("next").disabled = v === views.length - 1;
}
function go(d) { const nv = Math.min(views.length - 1, Math.max(0, v + d)); if (nv !== v) { v = nv; render(); } }
function relayout() { const first = views.length ? views[v][0] : 0; buildViews(); v = Math.max(0, views.findIndex(x => x.includes(first))); render(); }
document.getElementById("prev").onclick = () => go(-1);
document.getElementById("next").onclick = () => go(1);
document.addEventListener("keydown", e => { if (document.activeElement.isContentEditable) return; if (e.key === "ArrowRight") go(1); if (e.key === "ArrowLeft") go(-1); });
let sx = null;
document.addEventListener("touchstart", e => sx = e.touches[0].clientX, { passive: true });
document.addEventListener("touchend", e => { if (sx === null) return; const dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 50) go(dx < 0 ? 1 : -1); sx = null; });
window.addEventListener("resize", relayout);
relayout();
