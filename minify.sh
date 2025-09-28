#!/usr/bin/env bash
set -euo pipefail

SRC_DIR="rp2040-firmware"
OUT_DIR="tmp"

mkdir -p "$OUT_DIR"

find "$SRC_DIR" -type f -name "*.py" | while read -r f; do
    out="$OUT_DIR/${f#"$SRC_DIR"/}"
    mkdir -p "$(dirname "$out")"
    pyminify --remove-literal-statements "$f" -o "$out"
done

echo "✅ Arquivos minificados salvos em $OUT_DIR/"
