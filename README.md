# Wildmeshing

## Building

### Prerequisites

- CMake 3.10 or higher
- A C++17 compatible compiler
- Git

### Build Steps

#### 1. Clone the repository:

```bash
git clone https://github.com/wildmeshing/wildmeshing.git
cd wildmeshing
```

#### 2. Install requirements:

```bash
pip install -r requirements.txt
```

#### 3. Generate MD files from JSON files:

```bash
TODO
```

#### 4. Preview the documentation locally:

```bash
mkdocs serve
```

or

```bash
python -m mkdocs serve
```

## Adding a new component to the toolkit

Every component is expected to have a `"${component_name}_spec.json"` file in the `wildmeshing-toolkit/components` directory. The `generate_doc.py` script will automatically generate the corresponding markdown file in the `doc/toolkit_specs` directory. The generated markdown must be added manually to the `mkdocs.yml` file in order to be included in the documentation.
