import glob
import subprocess
import os


toolkit_path = f"{os.getcwd()}/toolkit"


includes = [f"{toolkit_path}/components"]
for f in glob.glob(f"{toolkit_path}/components/wmtk_components/*", recursive=True):
    name = os.path.basename(f)
    includes.append(f"{f}/wmtk/components/{name}")

command = ["python", "./json-spec-engine/docs/spec2html.py", "-i", f"{toolkit_path}/components/wmtk_components/main/wmtk/components/components.json", "--include-dirs"]
command += includes
command += ["-o", "./docs/_json_spec.md"]
subprocess.run(command)

command = ["python", "./json-spec-engine/scripts/generate_defaults.py", "-i", f"{toolkit_path}/components/wmtk_components/main/wmtk/components/components.json", "--include-dirs"]
command += includes
command  = ["-o", "./docs/_json_defaults.json"]
subprocess.run(command)