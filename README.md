# Wildmeshing

https://wildmeshing.github.io/ redirects to the documentation of the
[Wildmeshing Toolkit](https://github.com/wildmeshing/wildmeshing-toolkit), published at
https://wildmeshing.github.io/wildmeshing-toolkit/ from the toolkit's own repository (`docs/`,
`mkdocs.yml`). The toolkit replaces TetWild, fTetWild, TriWild and the wildmeshing-python
bindings this site used to document.

`public/` holds the redirect pages: the home page, the old pages (`tetwild/`, `ftetwild/`,
`triwild/`, `python/`, `wildmeshing/`) to their counterparts in the toolkit's documentation, and
`404.html` for any other old link. A push to `doc` publishes `public/` to `main`, the branch
GitHub Pages serves (`.github/workflows/build.yml`).
