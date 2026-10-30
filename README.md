# Wildmeshing

## Building

### Prerequisites

- Python 3
- Git

### Build Steps

#### 1. Clone the repository:

```bash
git clone -b doc https://github.com/wildmeshing/wildmeshing.github.io.git
cd wildmeshing.github.io
```

#### 2. Install requirements:

```bash
pip install -r requirements.txt
```

#### 3. Preview the documentation locally:

```bash
mkdocs serve
```

or

```bash
python -m mkdocs serve
```

## The Wildmeshing Toolkit's documentation

The toolkit's documentation, including the reference generated from its components'
`*_spec.json` files, is built from the toolkit's own repository (`docs/`, `mkdocs.yml`) and
published at https://wildmeshing.github.io/wildmeshing-toolkit/. This site links to it.
