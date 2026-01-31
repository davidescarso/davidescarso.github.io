#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMG_DIR="$ROOT_DIR/assets/images/random"
OUT_FILE="$ROOT_DIR/assets/js/random_images.js"
SOURCES_FILE="$ROOT_DIR/assets/js/image_sources.js"

if [[ ! -d "$IMG_DIR" ]]; then
  echo "Missing folder: $IMG_DIR" >&2
  exit 1
fi

mapfile -t files < <(find "$IMG_DIR" -maxdepth 1 -type f \( \
  -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.webp" -o -iname "*.gif" \
  \) -printf "%f\n" | sort)

{
  echo "window.RANDOM_IMAGES = ["
  for f in "${files[@]}"; do
    printf "  \"assets/images/random/%s\",\n" "$f"
  done
  echo "];"
} > "$OUT_FILE"

echo "Wrote $((${#files[@]})) entries to $OUT_FILE"

python3 - <<'PY'
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
img_dir = root / "assets" / "images" / "random"
sources_file = root / "assets" / "js" / "image_sources.js"

def load_sources(path: Path) -> dict:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8").strip()
    if text.startswith("window.IMAGE_SOURCES"):
        text = text.split("=", 1)[1].strip()
    if text.endswith(";"):
        text = text[:-1].strip()
    try:
        return json.loads(text) if text else {}
    except json.JSONDecodeError:
        return {}

sources = load_sources(sources_file)
files = sorted([p.name for p in img_dir.iterdir() if p.is_file()])
for name in files:
    if name not in sources:
        sources[name] = {"description": "", "source": "", "url": ""}

payload = json.dumps(sources, indent=2, ensure_ascii=True)
sources_file.write_text(f"window.IMAGE_SOURCES = {payload};\n", encoding="utf-8")
print(f"Synced {len(files)} images into {sources_file}")
PY
