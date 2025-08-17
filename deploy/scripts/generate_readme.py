import yaml
import string
from pathlib import Path

basedir = Path(__file__).parent.parent.parent

with open(Path(basedir, "assets/md/README.md"), encoding="utf-8") as f:
    tmpl = string.Template(f.read())

if not tmpl.is_valid():
    exit(1)

for p in basedir.glob("boards/**/*.zmk.yml"):
    f = open(p, "r", encoding="utf-8")
    metadata = yaml.SafeLoader(f).get_data()
    f.close()

    metadata["featurelist"] = ", ".join(metadata.pop("features"))

    with open(Path(p.parent, "README.md"), "w", encoding="utf-8") as f:
        f.write(tmpl.safe_substitute(metadata))
