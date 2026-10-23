#!/usr/bin/env python3
"""Offline release checks; not a substitute for licensing review or server E2E."""
from __future__ import annotations
import hashlib
from pathlib import Path
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {"SkullCreatorAPI-3.2.0/SkullCreatorAPI-3.2.0-SkiF4er.jar"}
HASH_FILE = ROOT / "SkullCreatorAPI-3.2.0" / "SHA256SUMS.txt"

def fail(why):
    print(f"FAIL: {why}", file=sys.stderr)
    raise SystemExit(1)

def validate_jar(path):
    try:
        with zipfile.ZipFile(path) as archive:
            if archive.testzip() is not None:
                fail(f"Corrupt ZIP entry in {path.name}")
            if not any(x.endswith(".class") for x in archive.namelist()):
                fail(f"No class files in {path.name}")
    except (OSError, zipfile.BadZipFile) as e:
        fail(f"Invalid JAR {path}: {e}")

actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file() and p.suffix.lower() == ".jar"}
if actual != ALLOWED:
    fail(f"JAR allowlist mismatch: expected {sorted(ALLOWED)}, found {sorted(actual)}")
for relative in ALLOWED:
    validate_jar(ROOT / relative)

entries = [line.strip() for line in HASH_FILE.read_text(encoding="utf-8").splitlines() if line.strip()]
if len(entries) != 1:
    fail("Expected exactly one checksum for SkullCreatorAPI")
match = re.fullmatch(r"([a-f0-9]{64})  ([A-Za-z0-9_.-]+)", entries[0])
if not match:
    fail("Incorrect checksum format")
checksum, filename = match.groups()
target = ROOT / "SkullCreatorAPI-3.2.0" / filename
if target.relative_to(ROOT).as_posix() not in ALLOWED:
    fail("Checksum points to an unapproved artifact")
if hashlib.sha256(target.read_bytes()).hexdigest() != checksum:
    fail("Checksum mismatch")

for path in [ROOT / "LICENSE", ROOT / "SkullCreatorAPI-3.2.0/LICENSE.txt", ROOT / "ExcellentCrates-6.6.1/LICENSE"]:
    if not path.exists() or path.stat().st_size < 1000:
        fail(f"License missing or empty: {path.relative_to(ROOT)}")
for p in [ROOT / "README.md", ROOT / "THIRD_PARTY_NOTICES.md"]:
    if not p.exists():
        fail(f"Required document missing: {p.name}")
    for rel in re.findall(r"\[[^]]+\]\(([^)]+)\)", p.read_text(encoding="utf-8")):
        if not rel.startswith(("https://", "http://", "#")) and not (p.parent / rel.split("#",1)[0]).exists():
            fail(f"Broken document link: {p.name} -> {rel}")

source = (ROOT / "ExcellentCrates-6.6.1/src/main/java/su/nightexpress/excellentcrates/hologram/handler/HologramPacketsHandler.java").read_text(encoding="utf-8")
patch = (ROOT / "ExcellentCrates-6.6.1/patches/hologram-vector-fix.patch").read_text(encoding="utf-8")
if "new Vector3d(0.0D, 0.0D, 0.0D)" not in source or "-        return new WrapperPlayServerSpawnEntity" not in patch:
    fail("Missing expected source fix or patch")
if "NitroSetupsPlayerProfile" in (ROOT / "README.md").read_text(encoding="utf8"):
    fail("Restricted plugin mentioned in public README")
print("PASS: public allowlist, SHA256, JAR integrity, licenses, source patch and document links")
