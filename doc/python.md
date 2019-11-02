Wildmeshing
===========

[![Anaconda-Server Badge](https://anaconda.org/conda-forge/wildmeshing/badges/downloads.svg)](https://anaconda.org/conda-forge/wildmeshing)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/wildmeshing/badges/installer/conda.svg)](https://conda.anaconda.org/conda-forge)

Wildmeshing is a simple and robust 2d and 3d meshing package.

It can be easily install trough conda:
```bash
conda install wildmeshing
```

[Jupyter Notebook](https://github.com/wildmeshing/wildmeshing-python/blob/master/examples/tutorial.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/wildmeshing/wildmeshing-python/master?filepath=examples%2Ftutorial.ipynb)



## Documentation

It has 4 main functions:

- `tetrahedralize`
- `triangulate`
- `triangulate_data`
- `triangulate_svg`


and an unique import
```python
import wildmeshing as wm
```

### File based API


`tetrahedralize` and `triangulate` takes as input a path and write the output to a file using these parameters

- `input`:  Input segments in .obj format (for `triangulate`) and input surface mesh in .off/.obj/.stl/.ply format (for `tetrahedralize`).
- `feature_input` default "": Input feature json file (only for `triangulate`)
- `output`, default "": output path


`triangulate_svg` reads an SVG and returns `numpy` arrays:

- `svg_path`: Path for the input SVG file

#### Examples:

High-order triangulating an SVG:
```python
V, F, nodes, F_nodes = wm.triangulate_svg("rocket.svg", cut_outside=True, hole_pts=[[255, 165]])
```

Tetrahedralizing an input triangle soup:
```python
wm.tetrahedralize("small.stl", "out.msh")
```

### `numpy` based API

`triangulate_data` uses `numpy` arrays as input and output:

- `V`: Input vertices
- `E`: Input edges
- `feature_info`, default `none`: Json string containing the features


#### Examples:

Triangulating vertex and edges:

```python
V = np.array([...])
L = np.array([...])

vs, tris, _, _ = wm.triangulate(V, L, cut_outside=True)

```


## Common options


All function have a common list of parameters:

- `stop_quality`, default -1: Specify max AMIPS energy for stopping mesh optimization
- `max_its`, default 80: Max number of mesh optimization iterations
- `stage`, default 1 in 2D and 2 in 3D: Specify envelope stage
- `epsilon`, default -1: Relative envelope $\epsilon_r$. Absolute $\epsilon = \epsilon_r \cdot d$, where $d$ is the diagonal of the bounding box
- `edge_length_r`, default 1/20: Relative target edge length $\ell_r$. Absolute $\ell=\ell_r \cdot d$,  where $d$ is the diagonal of the bounding box
- `mute_log`, default false: Mute prints



### Triangulation

The 2D meshing supports high order, therefore it has these additional options:

- `feature_epsilon`, default 1e-3: Relative feature envelope mu_r. Absolute mu, default mu_r * diagonal_of_bbox (only for `triangulate`)
- `flat_feature_angle`, default 10: Desired minimal angle
- `cut_outside`, default false: Remove "outside part"
- `skip_eps`, default false: Skip saving eps
- `hole_file`, default "": Input a .xyz file for specifying points inside holes you want to remove



### Tetrahedralization (alpha)


The tetrahedralization part is still under developement, for the moment it supports only files as input and output. Since it is more costly and complicated it has an additional input:

- `skip_simplify`, default false: Skips the mesh simplification