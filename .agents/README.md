# Project notes for agents

## Project overview

- Personal static website published to Neocities and GitHub Pages.
- Built with Jekyll 4.4.1, Liquid 4.0.4, Minima, and `jekyll-feed`; dependencies are managed with Bundler (`Gemfile` and `Gemfile.lock`).
- `_config.yml` enables the `musiclinks`, `videolinks`, `tweets`, `blogentries`, `concertlog`, `survivorranking`, and `albums2024` collections.
- Most public pages live under `pages/`; reusable Liquid layouts and includes live under `_layouts/` and `_includes/`. Collection entries use the `post` layout.
- Static content and media are important parts of the site. Do not remove, relocate, or rename assets as a performance shortcut without explicit scope and checking references.

## Build and validation

Run commands from the repository root:

```sh
bundle exec jekyll build
bundle exec jekyll serve
bundle exec jekyll serve --incremental
bundle exec jekyll build --profile
```

`--profile` reports time by build phase and Liquid template. Compare generated output as well as elapsed time when changing templates; `feed.xml` includes a build-time timestamp, so normalize its `<updated>` value for byte comparisons.

## Performance finding

The shared default layouts include `_includes/show_drawings.html`. Collection entries using `post` do not produce individual output pages, but their layout is still rendered. Rendering the drawings gallery for those entries was the main measured bottleneck: the include ran 291 times and took about 49 seconds in a profiled production build. The layouts now skip the gallery for `post` records; keep that guard in both `_layouts/default.html` and `_layouts/default_en.html` so the published homepages retain the widget without repeating the gallery during collection rendering.

On the measured Windows environment, a clean build improved from about 71 seconds (70.995 seconds profiled) to about 3 seconds (2.919 seconds profiled). The original and optimized outputs each contained 629 files and matched after normalizing the feed timestamp. Treat these numbers as a reference, not as a guaranteed CI or developer-machine target.

## Deployment and change guidance

- `.github/workflows/neocities.yml` builds with `JEKYLL_ENV=production`, deploys `_site` to Neocities and Nekoweb, and already enables Ruby Bundler caching via `ruby/setup-ruby`.
- Keep local builds and both deployment outputs working when changing Jekyll configuration or collection behavior.
- Prefer profiling before optimizing Liquid, especially templates that loop over `site.static_files` or nest collection loops.
- The documented deployment is Jekyll/Bundler-based; no separate JavaScript package build is required for the site.

## Strawpage drawing submissions

- `https://berbardo.straw.page/` currently sends a CSP `frame-ancestors` policy allowing only Strawpage origins and two localhost origins. It does not allow this site's homepage to frame it; the parent page cannot override that policy.
- No public Strawpage embed/allowlist guidance was found. Keep the drawing-submission path as an external link in both `_layouts/default.html` and `_layouts/default_en.html` unless Strawpage provides a supported way to allow this site's origin.
- Links should open in a new tab with `rel="noopener noreferrer"`. `.drawbook-link` styling and keyboard focus indication are in `css/drawings.css`.
