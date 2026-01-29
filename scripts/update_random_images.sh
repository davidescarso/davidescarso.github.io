#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMG_DIR="$ROOT_DIR/assets/images/random"
OUT_FILE="$ROOT_DIR/assets/js/random_images.js"

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
