#!/usr/bin/env bash
set -euo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
upstream="https://github.com/nulli0n/ExcellentCrates-spigot.git"
commit="d9ba2393a5dc812368379acc907f61a34aabb7bb"
source_path="src/main/java/su/nightexpress/excellentcrates/hologram/handler/HologramPacketsHandler.java"
expected_blob="d42288ce2da9ce82450454057432d8804b26f029"
dest="${1:-$repo_root/build/excellentcrates-6.6.1-source}"
if [[ -e "$dest" ]]; then echo "Refusing to overwrite: $dest" >&2; exit 2; fi
mkdir -p "$(dirname "$dest")"
git clone --no-checkout "$upstream" "$dest"
git -C "$dest" checkout --detach "$commit"
actual_blob="$(git -C "$dest" hash-object "$source_path")"
if [[ "$actual_blob" != "$expected_blob" ]]; then
 echo "Upstream source hash mismatch: $actual_blob" >&2; exit 3
fi
git -C "$dest" apply --check "$repo_root/ExcellentCrates-6.6.1/patches/hologram-vector-fix.patch"
git -C "$dest" apply "$repo_root/ExcellentCrates-6.6.1/patches/hologram-vector-fix.patch"
cmp "$dest/$source_path" "$repo_root/ExcellentCrates-6.6.1/$source_path"
echo "Patched source ready: $dest"
echo "Build can be attempted with Java 21 and Maven: cd '$dest' && mvn package"
