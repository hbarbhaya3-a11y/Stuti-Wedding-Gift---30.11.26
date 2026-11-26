import json, os, sys

OUT = sys.argv[1]

FONTS = "https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,wght@0,400;0,700;0,900;1,400&family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&family=Great+Vibes&family=Caveat:wght@400;700&family=Bebas+Neue&family=Old+Standard+TT:ital,wght@0,400;0,700;1,400&family=UnifrakturMaguntia&family=Inter:wght@300;400;600&family=Pacifico&family=Rubik+Mono+One&display=swap"

THEMES = {
 "coquette": dict(name="Pink Coquette", mast="FOREVER", cover="mag",
   bg1="#ffe3ea", bg2="#ffd0dc", ink="#7a1f42", ink2="#7a1f42", accent="#d6336c", accent2="#ffb3c7", paper="#ffffff",
   display="'Pacifico',cursive", script="'Great Vibes',cursive", body="'Playfair Display',serif", label="'Bebas Neue',sans-serif", mastfont="'Bodoni Moda',serif",
   pat1="linear-gradient(45deg,#ffd0dc 25%,transparent 25%,transparent 75%,#ffd0dc 75%),linear-gradient(45deg,#ffd0dc 25%,transparent 25%,transparent 75%,#ffd0dc 75%)", patsize="10cqw 10cqw", patpos="0 0,5cqw 5cqw",
   pat2="radial-gradient(#ffb3c7 18%,transparent 19%)", patsize2="6cqw 6cqw",
   frame="polaroid", filt="none", stickers=["🎀","🍒","💗","🌷","🎀","💌"], film="#d6336c"),
 "newspaper": dict(name="Vintage Newspaper", mast="The Forever Chronicle", cover="news",
   bg1="#f1e8d6", bg2="#ebe0c9", ink="#1d1a16", ink2="#1d1a16", accent="#1d1a16", accent2="#8b7d6b", paper="#f7f0e1",
   display="'Playfair Display',serif", script="'Old Standard TT',serif", body="'Old Standard TT',serif", label="'Old Standard TT',serif", mastfont="'UnifrakturMaguntia',serif",
   pat1="none", patsize="auto", patpos="0 0", pat2="none", patsize2="auto",
   frame="plain", filt="grayscale(1) sepia(.3)", stickers=[], film="#1d1a16"),
 "romance": dict(name="Red & Black Romance", mast="FOREVER", cover="mag",
   bg1="#7d0c1c", bg2="#111111", ink="#ffffff", ink2="#ffffff", accent="#e03150", accent2="#ffb3b3", paper="#ffffff",
   display="'Pacifico',cursive", script="'Great Vibes',cursive", body="'Playfair Display',serif", label="'Bebas Neue',sans-serif", mastfont="'Bebas Neue',sans-serif",
   pat1="none", patsize="auto", patpos="0 0", pat2="none", patsize2="auto",
   frame="stamp", filt="none", stickers=["🌹","❤️","🌹","💋","❤️","🌹"], film="#111"),
 "minimal": dict(name="Minimal Beige", mast="Forever", cover="mag",
   bg1="#f4ede3", bg2="#ece2d4", ink="#4a3f35", ink2="#4a3f35", accent="#8a6e52", accent2="#c7b29a", paper="#fbf7f1",
   display="'Great Vibes',cursive", script="'Great Vibes',cursive", body="'Playfair Display',serif", label="'Inter',sans-serif", mastfont="'Bodoni Moda',serif",
   pat1="none", patsize="auto", patpos="0 0", pat2="none", patsize2="auto",
   frame="thin", filt="saturate(.85)", stickers=[], film="#8a6e52"),
 "lavender": dict(name="Lavender Dream", mast="FOREVER", cover="mag",
   bg1="#efe6fb", bg2="#e3d4f7", ink="#4b2a7a", ink2="#4b2a7a", accent="#7b4fc9", accent2="#c9b1f0", paper="#ffffff",
   display="'Great Vibes',cursive", script="'Great Vibes',cursive", body="'Playfair Display',serif", label="'Bebas Neue',sans-serif", mastfont="'Bodoni Moda',serif",
   pat1="linear-gradient(90deg,rgba(123,79,201,.08) 50%,transparent 50%),linear-gradient(rgba(123,79,201,.08) 50%,transparent 50%)", patsize="8cqw 8cqw", patpos="0 0",
   pat2="radial-gradient(rgba(123,79,201,.18) 15%,transparent 16%)", patsize2="7cqw 7cqw",
   frame="rounded", filt="none", stickers=["🦋","💜","🌷","🎀","🦋","💜"], film="#7b4fc9"),
 "ocean": dict(name="Blue Gingham Ocean", mast="FOREVER", cover="mag",
   bg1="#e8f0fb", bg2="#d6e4f7", ink="#1f3d6e", ink2="#1f3d6e", accent="#2c5aa0", accent2="#9cbbe6", paper="#ffffff",
   display="'Playfair Display',serif", script="'Great Vibes',cursive", body="'Playfair Display',serif", label="'Bebas Neue',sans-serif", mastfont="'Bodoni Moda',serif",
   pat1="linear-gradient(90deg,rgba(44,90,160,.13) 50%,transparent 50%),linear-gradient(rgba(44,90,160,.13) 50%,transparent 50%)", patsize="6cqw 6cqw", patpos="0 0",
   pat2="linear-gradient(90deg,rgba(44,90,160,.2) 50%,transparent 50%),linear-gradient(rgba(44,90,160,.2) 50%,transparent 50%)", patsize2="10cqw 10cqw",
   frame="lace", filt="none", stickers=["⭐","🐚","🌊","⭐","🦋","🐚"], film="#1f3d6e"),
 "sunflower": dict(name="Sunflower Yellow", mast="FOREVER", cover="mag",
   bg1="#fff6cf", bg2="#ffe98a", ink="#6b4e00", ink2="#6b4e00", accent="#e0a400", accent2="#ffd84d", paper="#ffffff",
   display="'Pacifico',cursive", script="'Caveat',cursive", body="'Playfair Display',serif", label="'Bebas Neue',sans-serif", mastfont="'Bodoni Moda',serif",
   pat1="radial-gradient(rgba(224,164,0,.22) 14%,transparent 15%)", patsize="8cqw 8cqw", patpos="0 0",
   pat2="linear-gradient(90deg,rgba(255,255,255,.35) 50%,transparent 50%),linear-gradient(rgba(255,255,255,.35) 50%,transparent 50%)", patsize2="8cqw 8cqw",
   frame="polaroid", filt="saturate(1.1)", stickers=["🌻","🌼","🧸","☀️","🌻","🌼"], film="#6b4e00"),
 "vintage": dict(name="Vintage Scrapbook", mast="Forever", cover="mag",
   bg1="#e9dcc3", bg2="#dcc9a6", ink="#4a2f17", ink2="#4a2f17", accent="#8b5a2b", accent2="#c9a56f", paper="#f6eedd",
   display="'Playfair Display',serif", script="'Caveat',cursive", body="'Old Standard TT',serif", label="'Old Standard TT',serif", mastfont="'Playfair Display',serif",
   pat1="repeating-linear-gradient(0deg,rgba(74,47,23,.04) 0 .4cqw,transparent .4cqw 1.2cqw)", patsize="auto", patpos="0 0",
   pat2="radial-gradient(rgba(74,47,23,.08) 20%,transparent 21%)", patsize2="4cqw 4cqw",
   frame="torn", filt="sepia(.45) saturate(.9)", stickers=["🦋","🕰️","🍂","🌾","🦋","✉️"], film="#4a2f17"),
 "editorial": dict(name="Classic Glam Editorial", mast="FOREVER", cover="mag",
   bg1="#ffffff", bg2="#f3efe8", ink="#111111", ink2="#111111", accent="#b08d57", accent2="#d9c4a0", paper="#ffffff",
   display="'Bodoni Moda',serif", script="'Great Vibes',cursive", body="'Playfair Display',serif", label="'Inter',sans-serif", mastfont="'Bodoni Moda',serif",
   pat1="none", patsize="auto", patpos="0 0", pat2="none", patsize2="auto",
   frame="plain", filt="none", stickers=[], film="#111"),
 "travel": dict(name="Travel Photo-Dump", mast="FOREVER", cover="mag",
   bg1="#1c2233", bg2="#e8d9bf", ink="#ffffff", ink2="#2a2018", accent="#ff8a3d", accent2="#ffd27a", paper="#ffffff",
   display="'Bebas Neue',sans-serif", script="'Caveat',cursive", body="'Inter',sans-serif", label="'Bebas Neue',sans-serif", mastfont="'Bebas Neue',sans-serif",
   pat1="none", patsize="auto", patpos="0 0", pat2="repeating-linear-gradient(0deg,rgba(0,0,0,.03) 0 .3cqw,transparent .3cqw 1cqw)", patsize2="auto",
   frame="cutout", filt="saturate(1.1) contrast(1.05)", stickers=["✈️","📸","🌅","🗺️","🌴","✨"], film="#111"),
 "y2k": dict(name="Y2K Bubble Pink", mast="FOREVER", cover="mag",
   bg1="#fbe3f4", bg2="#e9d8ff", ink="#8a1f6b", ink2="#5a2a9a", accent="#ff4fae", accent2="#b88cff", paper="#ffffff",
   display="'Pacifico',cursive", script="'Pacifico',cursive", body="'Inter',sans-serif", label="'Rubik Mono One',sans-serif", mastfont="'Rubik Mono One',sans-serif",
   pat1="radial-gradient(circle at 20% 20%,rgba(255,255,255,.9),transparent 22%),radial-gradient(circle at 80% 70%,rgba(184,140,255,.35),transparent 30%),linear-gradient(135deg,#ffd6f0,#e2d4ff 50%,#cdeeff)", patsize="auto", patpos="0 0",
   pat2="radial-gradient(circle,rgba(255,255,255,.7) 12%,transparent 13%),linear-gradient(160deg,#ffc8ec,#d9c8ff)", patsize2="9cqw 9cqw,auto",
   frame="pearl", filt="saturate(1.1)", stickers=["🫧","💖","✨","🎀","🫧","💖"], film="#ff4fae"),
}

def ph(src, label, extra=""):
    return f'<div class="ph" data-src="../photos/{src}"{extra}><span>{label}<small>photos/{src}</small></span></div>'

def fr(src, label, style, cap=""):
    c = f'<em class="edit" contenteditable>{cap}</em>' if cap else ""
    return f'<div class="fr" style="{style}">{ph(src,label)}{c}</div>'

def st(t, i, style):
    s = t["stickers"]
    return f'<div class="sticker" style="{style}">{s[i % len(s)]}</div>' if s else ""

def cover(t):
    if t["cover"] == "news":
        return f'''<section class="page pa newscover">
  <div class="ntop"><span>Vol. I · No. 1</span><span data-fill="dateLong">DATE</span><span>Wedding Edition</span></div>
  <div class="flag">{t["mast"]}</div><div class="nrule"></div>
  <h1 class="edit" contenteditable>THE WEDDING<br>OF THE YEAR</h1>
  <h3 data-fill="couple">Name &amp; Name</h3>
  {fr("cover.jpg","COVER PHOTO","left:7cqw;right:7cqw;top:58cqw;height:62cqw")}
  <div class="ncap edit" contenteditable>Exclusive photographs inside · Pages 2–14</div>
</section>'''
    return f'''<section class="page cover">
  {ph("cover.jpg","COVER PHOTO")}
  <div class="mast edit" contenteditable>{t["mast"]}</div>
  <div class="issue">THE WEDDING ISSUE</div>
  <div class="lines">
    <b class="edit" contenteditable>Two Hearts,</b><p class="edit" contenteditable>one beautiful story</p>
    <b class="edit" contenteditable>Exclusive:</b><p class="edit" contenteditable>how it all began</p>
    <b class="edit" contenteditable>Our Playlist</b><p class="edit" contenteditable>songs that are “us”</p>
  </div>
  <div class="ed"><b data-fill="day">00</b><span data-fill="monthYear">MONTH 2027</span></div>
  <div class="names" data-fill="couple">Name &amp; Name</div>
  <div class="bottom">A SPECIAL EDITION · FOR MY FOREVER</div>
  <div class="barcode"><i></i></div>
</section>'''

def pages(t):
    P = [cover(t)]
    P.append(f'''<section class="page pa">
  <div class="lab" style="left:8cqw;top:8cqw">Chapter one</div>
  <h2 class="edit" contenteditable style="left:8cqw;right:8cqw;top:13cqw">How it all began</h2>
  {fr("story-1.jpg","PHOTO — your first photo together","left:10cqw;right:10cqw;top:40cqw;height:78cqw;--r:-2deg","where it started")}
  {st(t,0,"right:7cqw;top:34cqw")}
  <p class="txt edit" contenteditable style="left:10cqw;right:10cqw;top:126cqw;text-align:center">[Place · Year]</p>
</section>''')
    P.append(f'''<section class="page pb">
  <div class="lab" style="left:8cqw;top:8cqw">The story</div>
  <div class="cols edit" contenteditable style="left:8cqw;right:8cqw;top:14cqw">
    <p>[How you met.] It began on an ordinary day in [city], when [Partner] walked in and everything quietly changed. Write the real story here — the first conversation, the first impression, the moment you knew.</p>
    <p>[The first date.] It involved [place], [food] and a conversation that lasted far longer than planned.</p>
    <p>[The proposal.] On [date], at [place], the question was asked — and the answer was a very quick “yes”.</p>
    <p>[Today.] And now we begin our greatest chapter yet — together, forever.</p>
  </div>
  <div class="quote edit" contenteditable style="left:8cqw;right:8cqw;top:72cqw">“You are my favourite chapter.”</div>
  {fr("story-2.jpg","PHOTO — the proposal","left:14cqw;right:14cqw;top:90cqw;height:42cqw;--r:2deg")}
</section>''')
    P.append(f'''<section class="page pa">
  <h2 class="edit" contenteditable style="left:7cqw;top:6cqw;width:60cqw">our playlist</h2>
  <div class="player" style="left:8cqw;top:36cqw;width:46cqw">
    {ph("playlist.jpg","PHOTO",' style="position:relative;width:100%;aspect-ratio:1"')}
    <div class="t edit" contenteditable>[Our Song]</div><div class="a edit" contenteditable>[Artist]</div>
    <div class="bar"></div><div class="times"><span>1:42</span><span>3:58</span></div>
    <div class="ctrl"><span>⏮</span><span>⏸</span><span>⏭</span></div>
  </div>
  <ul class="tracks edit" contenteditable style="left:60cqw;top:40cqw;width:34cqw"><li>[Song 1]</li><li>[Song 2]</li><li>[Song 3]</li><li>[Song 4]</li><li>[Song 5]</li><li>[Song 6]</li></ul>
  {st(t,1,"right:7cqw;top:9cqw")}{st(t,2,"left:57cqw;top:28cqw")}
  <div class="note edit" contenteditable style="left:58cqw;top:100cqw;width:34cqw">same hearts,<br>same songs,<br>same us ♡</div>
</section>''')
    P.append(f'''<section class="page pb">
  <h2 class="edit" contenteditable style="right:7cqw;top:6cqw;text-align:right;width:70cqw">little moments</h2>
  {fr("moment-1.jpg","moment-1","left:7cqw;top:30cqw;width:40cqw;height:46cqw;--r:-5deg","coffee dates")}
  {fr("moment-2.jpg","moment-2","right:7cqw;top:50cqw;width:40cqw;height:46cqw;--r:4deg","late-night drives")}
  {fr("moment-3.jpg","moment-3","left:12cqw;top:86cqw;width:40cqw;height:42cqw;--r:-2deg","our silly faces")}
  {st(t,3,"right:10cqw;top:110cqw")}{st(t,4,"left:44cqw;top:72cqw")}
</section>''')
    P.append(f'''<section class="page pa">
  <div class="search" style="left:7cqw;right:7cqw;top:8cqw">
    <div class="logo">Lovely</div>
    <div class="box">🔍 <span class="edit" contenteditable>best fiancé in the world</span></div>
    <div class="tabs"><b>All</b><span>Images</span><span>Videos</span><span>News</span></div>
  </div>
  <div class="grid" style="left:7cqw;right:7cqw;top:42cqw;height:74cqw">
    {ph("search-1.jpg","search-1",' style="grid-row:span 2"')}{ph("search-2.jpg","search-2")}{ph("search-3.jpg","search-3")}{ph("search-4.jpg","search-4")}{ph("search-5.jpg","search-5")}
  </div>
  <p class="txt edit" contenteditable style="left:7cqw;right:7cqw;top:121cqw">About 1 result (0.00 seconds) — <b data-fill="partner">[Partner]</b>. There is only one, and I'm marrying him.</p>
</section>''')
    P.append(f'''<section class="page pb">
  {fr("who-main.jpg","MAIN PHOTO","left:7cqw;top:7cqw;width:52cqw;height:70cqw;--r:0deg")}
  {fr("who-2.jpg","who-2","right:7cqw;top:7cqw;width:28cqw;height:33cqw;--r:3deg")}
  {fr("who-3.jpg","who-3","right:7cqw;top:44cqw;width:28cqw;height:33cqw;--r:-3deg")}
  <h2 class="big edit" contenteditable style="right:7cqw;bottom:8cqw;text-align:right">Who's<br>that<br>guy?</h2>
  <p class="txt edit" contenteditable style="left:7cqw;top:88cqw;width:36cqw">[Three words that describe him.] Kind. Funny. Mine. Write a few lines about what makes him, him.</p>
  {st(t,5,"left:50cqw;top:80cqw")}
</section>''')
    P.append(f'''<section class="page alt">
  <div class="lab big2 edit" contenteditable style="left:7cqw;top:7cqw">CHAAR KADAM</div>
  <h2 class="edit" contenteditable style="left:7cqw;top:15cqw;width:86cqw">bas chaar kadam…</h2>
  {fr("lyric.jpg","PHOTO","left:12cqw;right:12cqw;top:42cqw;height:70cqw;--r:-2deg")}
  {st(t,0,"right:8cqw;top:40cqw")}
  <p class="txt edit" contenteditable style="left:10cqw;right:10cqw;top:122cqw;text-align:center">[A favourite song lyric or a line just for him.]</p>
</section>''')
    P.append(f'''<section class="page pa">
  <div class="filmstrip" style="left:7cqw;top:7cqw;width:34cqw;bottom:7cqw">
    {ph("film-1.jpg","film-1")}{ph("film-2.jpg","film-2")}{ph("film-3.jpg","film-3")}{ph("film-4.jpg","film-4")}
  </div>
  <div class="heart" style="right:10cqw;top:12cqw;width:38cqw"></div>
  <div class="lab big2 edit" contenteditable style="right:7cqw;top:58cqw;text-align:right">TU MERI<br>DUNIYA</div>
  <p class="txt edit" contenteditable style="left:47cqw;right:7cqw;top:82cqw">[A memory only the two of you share — the trip, the fight you laughed about, the night everything felt right.]</p>
</section>''')
    P.append(f'''<section class="page pb">
  <div class="lab" style="left:12cqw;top:8cqw">Our journey</div>
  <h2 class="edit" contenteditable style="left:10cqw;right:8cqw;top:13cqw">from hello to forever</h2>
  <div class="timeline edit" contenteditable>
    <div><b>[YEAR]</b><span>We met</span><small>[Where and how]</small></div>
    <div><b>[YEAR]</b><span>First date</span><small>[What you did]</small></div>
    <div><b>[YEAR]</b><span>First trip</span><small>[Where you went]</small></div>
    <div><b>[YEAR]</b><span>The proposal</span><small>[The moment]</small></div>
    <div><b data-fill="year">[YEAR]</b><span>Forever begins</span><small>Our wedding day</small></div>
  </div>
</section>''')
    P.append(f'''<section class="page pa">
  <div class="arch" style="left:14cqw;right:14cqw;top:8cqw;height:88cqw">{ph("wedding.jpg","WEDDING PHOTO")}</div>
  <h2 class="edit" contenteditable style="left:0;right:0;top:100cqw;text-align:center">Happy Wedding</h2>
  <div class="lab" style="left:0;right:0;top:120cqw;text-align:center" data-fill="coupleCaps">NAME &amp; NAME</div>
  <div class="lab" style="left:0;right:0;top:126cqw;text-align:center" data-fill="dateLong">DATE</div>
</section>''')
    P.append(f'''<section class="page letter">
  <h2 class="edit" contenteditable style="left:16cqw;top:7cqw">A letter to you</h2>
  <div class="body edit" contenteditable>My love,<br><br>[Write your letter here. What you felt the first time you saw him, what you love most, what you promise for the years ahead.]<br><br>Thank you for choosing me, every single day.<br><br>Forever yours,<br><span data-fill="you">[Your Name]</span> ♡</div>
</section>''')
    strips = "".join(
        f'<div class="filmstrip booth" style="left:{x}cqw;top:{y}cqw;width:26cqw;bottom:{b}cqw;transform:rotate({r}deg)">' +
        "".join(ph(f"booth-{n}.jpg", str(n)) for n in range(k, k + 4)) + "</div>"
        for x, y, b, r, k in [(8, 26, 8, -3, 1), (37, 24, 10, 2, 5), (66, 27, 7, -1.5, 9)])
    P.append(f'''<section class="page alt">
  <h2 class="edit" contenteditable style="left:0;right:0;top:6cqw;text-align:center">photo dump</h2>
  {strips}
</section>''')
    P.append(f'''<section class="page back">
  {ph("back.jpg","BACK COVER PHOTO")}<div class="shade"></div>
  <div class="card"><h2 class="edit" contenteditable>You're my home</h2><div class="t edit" contenteditable>The One &amp; Only</div><div class="a" data-fill="couple">Name &amp; Name</div><div class="bar"></div><div class="ctrl"><span>⏮</span><span>⏸</span><span>⏭</span></div></div>
</section>''')
    return "\n".join(P)

CSS = open(os.path.join(os.path.dirname(__file__), "theme.css")).read()
JS = open(os.path.join(os.path.dirname(__file__), "book.js")).read()

for key, t in THEMES.items():
    vars_ = ";".join(f"--{k}:{t[k]}" for k in ["bg1","bg2","ink","ink2","accent","accent2","paper","display","script","body","label","mastfont","pat1","patsize","patpos","pat2","patsize2","filt","film"])
    html = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="robots" content="noindex, nofollow, noarchive">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Forever — {t["name"]}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<style>:root{{{vars_}}}
{CSS}</style></head>
<body class="f-{t["frame"]} t-{key}">
<a class="home" href="../">← all styles</a>
<div class="stage"><div class="book" id="book">
{pages(t)}
</div></div>
<nav><button id="prev" aria-label="Previous">‹</button><span id="count"></span><button id="next" aria-label="Next">›</button></nav>
<script src="../config.js"></script>
<script>{JS}</script>
</body></html>'''
    os.makedirs(os.path.join(OUT, key), exist_ok=True)
    open(os.path.join(OUT, key, "index.html"), "w").write(html)

json.dump({k: dict(name=v["name"], bg=v["bg1"], bg2=v["bg2"], accent=v["accent"], ink=v["ink"]) for k, v in THEMES.items()}, open(os.path.join(OUT, "themes.json"), "w"))
print("built", len(THEMES))
