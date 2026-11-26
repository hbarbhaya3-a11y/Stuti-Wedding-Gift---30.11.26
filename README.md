# Forever: The Wedding Issue

There are 12 versions of one 14-page flip-through wedding magazine: 11 that each use a single style, and 1 mixed version.
Open the hub page to pick one: `/s-2LkujtLw9VCy5qex/`

Styles: Mixed · Pink Coquette · Vintage Newspaper · Red & Black Romance · Minimal Beige · Lavender Dream · Blue Gingham Ocean · Sunflower Yellow · Vintage Scrapbook · Classic Glam Editorial · Travel Photo-Dump · Y2K Bubble Pink

## Edit once, used by every version
- **Names and date:** `s-2LkujtLw9VCy5qex/config.js`
- **Photos:** put them in `s-2LkujtLw9VCy5qex/photos/` using the file names printed on each placeholder (cover.jpg, story-1.jpg, moment-1.jpg, booth-1.jpg …). Every version picks them up.
- **Text:** the [bracketed] text in each `<style>/index.html`.

`_source/` holds the generator that builds the single-style versions (`python3 gen.py <folder>`).
