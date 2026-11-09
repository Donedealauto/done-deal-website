# Done Deal Auto Group website

`dist/` contains the website and its assets. `scripts/` contains the Python page generators, and `functions/api/` contains the Cloudflare Pages quote API.

Run `npm run build` to regenerate the HTML and `npm run check` to check the browser JavaScript. The generator requires Python 3; there are no npm dependencies.

For Cloudflare Pages, connect the GitHub repository, choose production branch `main`, use the repository root, choose no framework preset, set build command `exit 0`, and use `dist` as the output directory. Keep `functions/` at the repository root.

The form uses an email fallback until the Pages deployment is configured. See `.dev.vars.example` for the runtime variables. Set the Resend API key and Turnstile secret as encrypted values in Cloudflare. Use a verified sending address and run an end-to-end inbox test before launch.

## Media credits

Customer Stories hero footage: [A car driving down a highway in the desert](https://www.pexels.com/video/a-car-driving-down-a-highway-in-the-desert-28388458/) by Dubang chang, used under the [Pexels license](https://www.pexels.com/license/). The site uses a trimmed, muted copy and a still frame from the same clip.

Additional [Pexels](https://www.pexels.com/license/) hero footage, edited to short silent loops with matching still frames:

- Services: [Coastal highway](https://www.pexels.com/video/point-of-view-of-a-car-driving-along-a-highway-by-the-sea-15341834/) by Dimitri Baret.
- About: [Mountain road](https://www.pexels.com/video/point-of-view-of-a-car-driving-on-a-mountain-road-12365082/) by Dimitri Baret.
- Contact: [Open highway](https://www.pexels.com/video/point-of-view-of-a-car-driving-on-a-road-11367262/) by caner cevirgen.
