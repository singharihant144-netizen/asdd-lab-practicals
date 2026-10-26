# aa hacks

Responsive static study site with seven ASDD labs, 26 SMLDS Python experiments, four dataset CSVs, and 228 searchable viva questions with model answers. Each SMLDS script can be viewed, copied in full, or downloaded. Dataset CSVs and the complete SMLDS study pack are available on the site.

## Live site

https://singharihant144-netizen.github.io/asdd-lab-practicals/

GitHub Pages serves the root of the `main` branch. No build step or secrets are required.

## Files

- `index.html` — ASDD Lab, SMLDS Lab and Viva Prep tabs
- `app.js` — lab rendering, dataset and code catalogue, search, copy controls, viva filters and aa helper
- `viva-data.js`, `viva-data-smlds.js`, `smlds-data.js` — question banks, dataset facts and full copyable experiment source
- `style.css`, `style-viva.css`, `style-smlds.css` — responsive layout, motion and reduced-motion support
- `smlds/` — original Python files, dataset CSVs and README
- `smlds-study-pack.zip` — scripts and all four CSVs in one download
- `asdd-hack-aa2.docx`, `asdd-viva-questions.pdf` — original ASDD downloads

The supplied SMLDS scripts are preserved as submitted. Some use scikit-learn or Seaborn built-in data loaders and may need internet the first time. The supplied CSVs are available separately under `smlds/datasets/`.

The aa helper runs in the browser and uses the published ASDD/SMLDS guides and common troubleshooting checks; it is not connected to a hosted generative AI service.
