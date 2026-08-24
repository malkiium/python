from pathlib import Path
import re


script_dir = Path(__file__).resolve().parent

with open(script_dir / "aerospaceConfig.txt") as f:
    aerospace = f.readlines()

with open(script_dir / "frMacOSConfig.txt") as f:
    macos = {
        line.strip()
        for line in f
        if line.strip() and not line.lstrip().startswith("#")
    }

binding_pattern = re.compile(r"^\s*([a-z0-9]+(?:-[a-z0-9]+)*)\s*=")
bindings = {
    match.group(1)
    for line in aerospace
    if (match := binding_pattern.match(line))
}
conflicts = sorted(bindings & macos)

if conflicts:
    print(f"{len(conflicts)} protected shortcut(s) used by AeroSpace:")
    for modifier in ("alt-shift", "alt"):
        matching = [
            key
            for key in conflicts
            if key.startswith(f"{modifier}-")
            and (modifier == "alt-shift" or not key.startswith("alt-shift-"))
        ]
        if matching:
            print(f"{modifier}: {', '.join(matching)}")
else:
    print("No protected shortcuts are used by AeroSpace.")