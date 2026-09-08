"""Build an upload snapshot from the canonical BOOST skill; standard library only."""
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile

root = Path(__file__).resolve().parents[1]
source = root / "skills" / "boost-show-notes"
files = sorted(p for p in source.rglob("*") if p.is_file())
if not (source / "SKILL.md").is_file():
    raise SystemExit("Canonical SKILL.md is missing")

def git(*args):
    return subprocess.check_output(
        ["git", "-C", str(root), *args], text=True, encoding="utf-8"
    ).strip()

commit = git("rev-parse", "HEAD")
dirty = bool(git("status", "--porcelain", "--", "skills/boost-show-notes"))
output = root / "dist"
output.mkdir(exist_ok=True)
package = output / "boost-show-notes.skill"
hashes = {}
with zipfile.ZipFile(package, "w", zipfile.ZIP_DEFLATED) as archive:
    for path in files:
        data = path.read_bytes()
        name = path.relative_to(source.parent).as_posix()
        archive.writestr(name, data)
        hashes[name] = hashlib.sha256(data).hexdigest()
manifest = {
    "repository": "ulrikkerocks/BOOST",
    "commit": commit,
    "source_has_uncommitted_changes": dirty,
    "files_sha256": hashes,
    "package_sha256": hashlib.sha256(package.read_bytes()).hexdigest(),
}
(output / "boost-show-notes.source.json").write_text(
    json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
)
print(f"Created {package}")
if dirty:
    print("Draft snapshot: canonical skill has uncommitted changes.")
