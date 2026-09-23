#!/usr/bin/env python3
"""Builds the single uploadable .zip for people installing by hand in the Claude app.

The app's uploader accepts exactly one plugin.json per zip and ignores any marketplace.json
inside it. Both were confirmed by upload: a zip carrying a vendored dependency is rejected with
"Zip must contain exactly one plugin.json. Found 2", and a zip carrying a marketplace.json
installs the skills but never creates the connector. So the repo layout — a product plugin that
depends on a shared connection plugin by bare name — cannot survive an upload intact. There is
no marketplace for the bare name to resolve against, and it would fail silently.

This script therefore folds the dependency's mcpServers into the built manifest and drops the
dependencies array. That inversion is exactly what verify-plugin-manifests.py forbids in the
repo, which is correct: the repo keeps the split so the marketplace install path still dedupes,
and only this build output collapses it. Never copy the built manifest back over the source.

The collapse is safe because Claude Code keys plugin MCP servers by URL, not by server name or
plugin name: two plugins pointing at one URL resolve to a single connection. Verified against
`claude mcp list`, which listed one entry for two plugins sharing a URL under different server
keys, and two entries once the URLs differed. Not yet verified inside the Claude app.
"""
import json
import pathlib
import shutil
import sys
import urllib.error
import urllib.request
import zipfile

# Component directories the app loads. marketplace.json is deliberately absent: the app ignores
# it, and shipping one implies a dependency will resolve when it will not.
BUNDLED = ("skills", "agents", "commands", "workflows", "outputStyles")
DOCS = ("README.md", "INSTALL.md", "LICENSE")
GITHUB_ORG = "BotBuilders"
RAW = "https://raw.githubusercontent.com/{org}/{repo}/main/.claude-plugin/plugin.json"

root = pathlib.Path(__file__).resolve().parent.parent


def fail(msg: str) -> None:
    sys.exit(f"FAIL: {msg}")


def dependency_manifest(name: str) -> dict:
    """Read a dependency's manifest from the sibling checkout, else from GitHub.

    The sibling wins so a local edit to the connection plugin is picked up before it is pushed.
    """
    sibling = root.parent / name / ".claude-plugin" / "plugin.json"
    if sibling.is_file():
        print(f"  dependency {name}: {sibling}")
        return json.loads(sibling.read_text())

    url = RAW.format(org=GITHUB_ORG, repo=name)
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            print(f"  dependency {name}: {url}")
            return json.loads(resp.read())
    except (urllib.error.URLError, json.JSONDecodeError, OSError) as exc:
        fail(f"cannot read dependency {name!r}: no sibling checkout at {sibling.parent.parent} "
             f"and fetching {url} failed: {exc}")


manifest_path = root / ".claude-plugin" / "plugin.json"
if not manifest_path.is_file():
    fail(f"no {manifest_path.relative_to(root)}; this is not a plugin repo")

manifest = json.loads(manifest_path.read_text())
name = manifest["name"]
version = manifest.get("version", "0.0.0")
print(f"Building {name} {version}")

servers = dict(manifest.get("mcpServers") or {})
for dep in manifest.pop("dependencies", []):
    if "@" in dep:
        fail(f'dependency "{dep}" is marketplace-qualified; use the bare name.')
    for key, server in (dependency_manifest(dep).get("mcpServers") or {}).items():
        existing = servers.get(key)
        if existing and existing != server:
            fail(f"server {key!r} defined twice with different settings; rename one.")
        servers[key] = server

if servers:
    manifest["mcpServers"] = servers
else:
    print("  no MCP servers to fold in (skills-only plugin)")

stage = root / "dist" / name
shutil.rmtree(stage.parent, ignore_errors=True)
(stage / ".claude-plugin").mkdir(parents=True)
(stage / ".claude-plugin" / "plugin.json").write_text(
    json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)
for item in BUNDLED:
    if (root / item).is_dir():
        shutil.copytree(root / item, stage / item)
for doc in DOCS:
    if (root / doc).is_file():
        shutil.copy2(root / doc, stage / doc)

found = list(stage.rglob("plugin.json"))
if len(found) != 1:
    fail(f"zip would carry {len(found)} plugin.json; the app accepts exactly one.")

out = root / "dist" / f"{name}-{version}.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
    for path in sorted(stage.rglob("*")):
        if path.is_file() and path.name != ".DS_Store":
            zf.write(path, path.relative_to(stage))

print(f"OK: {out.relative_to(root)} ({out.stat().st_size:,} bytes)")
print(f"  servers: {', '.join(servers) or 'none'}")
print(f"  validate with: claude plugin validate {stage.relative_to(root)}")
