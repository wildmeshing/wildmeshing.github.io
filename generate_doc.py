import glob
import subprocess
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
toolkit_components = HERE / "toolkit" / "components"

DOCS_PATH = HERE / "doc"
DOCS_COMPONENTS_PATH = DOCS_PATH / "toolkit_specs"

if not DOCS_PATH.exists():
    print(f"Error: {DOCS_PATH} does not exist.")
    sys.exit(1)

if not DOCS_COMPONENTS_PATH.exists():
    os.makedirs(DOCS_COMPONENTS_PATH)

# iterate through all the components and generate the documentation for each one
for f in glob.glob(f"{toolkit_components}/*", recursive=True):
    name = os.path.basename(f)
    spec_file = toolkit_components / name / \
        "wmtk" / "components" / name / f"{name}_spec.json"

    if not spec_file.exists():
        continue

    print(f"Generating documentation for {name}...")

    md_file = DOCS_COMPONENTS_PATH / f"{name}_spec.md"
    md_defaults_file = DOCS_COMPONENTS_PATH / f"{name}_defaults.json"

    command = [sys.executable, "./json-spec-engine/docs/spec2html.py"]
    command += ["-i", f"{spec_file}"]
    command += ["-o", f"{md_file}"]
    command += ["--include-dirs", f"{spec_file.parent}"]
    subprocess.run(command)

    command = [sys.executable,
               "./json-spec-engine/scripts/generate_defaults.py"]
    command += ["-i", f"{spec_file}"]
    command += ["-o", f"{md_defaults_file}"]
    command += ["--include-dirs", f"{spec_file.parent}"]
    subprocess.run(command)
