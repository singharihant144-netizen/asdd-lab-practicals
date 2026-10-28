# aa hacks

Responsive static study site with seven ASDD labs, 26 SMLDS Python experiments, three WMC wireless simulations, four SMLDS dataset CSVs, and 258 searchable viva questions with model answers. Each SMLDS and WMC script can be viewed, copied in full, or downloaded. Dataset CSVs and subject study packs are available on the site.

## Live site

https://singharihant144-netizen.github.io/asdd-lab-practicals/

GitHub Pages serves the root of the `main` branch. No build step or secrets are required.

## Files

- `index.html` — ASDD Lab, SMLDS Lab, WMC Lab and Viva Prep tabs
- `app.js` — lab rendering, experiment catalogues, search, copy controls, viva filters and aa helper
- `viva-data.js`, `viva-data-smlds.js`, `viva-data-wmc.js`, `smlds-data.js`, `wmc-data.js` — question banks, dataset facts and full copyable experiment sources
- `style.css`, `style-viva.css`, `style-smlds.css`, `style-wmc.css` — responsive layout, motion and reduced-motion support
- `smlds/` — original Python files, dataset CSVs and README
- `smlds-study-pack.zip` — scripts and all four CSVs in one download
- `wmc/` — three original wireless simulation scripts and a run guide
- `wmc-viva-questions.md` — all 30 WMC questions and model answers
- `wmc-study-pack.zip` — all supplied WMC scripts, run guide, and viva questions
- `asdd-hack-aa2.docx`, `asdd-viva-questions.pdf` — original ASDD downloads

The supplied SMLDS and WMC scripts are preserved as submitted. Some SMLDS scripts use scikit-learn or Seaborn built-in data loaders and may need internet the first time. The supplied CSVs are available separately under `smlds/datasets/`. WMC simulations generate their signals and bits in Python; no separate database was included, and they require NumPy and Matplotlib.

The aa helper runs in the browser and uses the published ASDD/SMLDS/WMC guides and common troubleshooting checks; it is not connected to a hosted generative AI service.
