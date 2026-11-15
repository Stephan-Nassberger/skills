#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
CONTEXT="$ROOT/.claude/design-context.md"

if [ ! -f "$CONTEXT" ]; then
  echo "error: $CONTEXT not found." >&2
  echo "Ask the design skill to run its setup wizard first." >&2
  exit 1
fi

fm() {
  awk '/^---$/{n++; next} n==1' "$CONTEXT" \
    | grep -E "^$1:[[:space:]]*" \
    | head -1 \
    | sed -E "s/^$1:[[:space:]]*//; s/^\"(.*)\"$/\1/; s/^'(.*)'$/\1/"
}

FRAMEWORK="$(fm css_framework)"
PM="$(fm package_manager)"
ENTRY="$(fm tokens_entry_css)"
TOKENS="$(fm tokens_css)"
OUT_DIR="$(fm output_dir)"

: "${OUT_DIR:=design-mockups}"

require() {
  if [ -z "$2" ]; then
    echo "error: '$1' is empty in .claude/design-context.md" >&2
    exit 1
  fi
}

case "$PM" in
  pnpm) DLX="pnpm dlx" ;;
  yarn) DLX="yarn dlx" ;;
  bun)  DLX="bunx" ;;
  npm|"") DLX="npx --yes" ;;
  *)    DLX="npx --yes" ;;
esac

mkdir -p "$ROOT/$OUT_DIR"
cd "$ROOT"

# Relative prefix from $OUT_DIR back to the repo root ("../" per path segment).
REL="$(printf '%s' "$OUT_DIR" | awk -F/ '{for (i = 1; i <= NF; i++) printf "../"}')"

case "$FRAMEWORK" in
  tailwind-v4)
    require tokens_entry_css "$ENTRY"
    if [ ! -f "$OUT_DIR/_input.css" ]; then
      printf '@import "%s%s";\n@source ".";\n' "$REL" "$ENTRY" > "$OUT_DIR/_input.css"
    fi
    $DLX @tailwindcss/cli@latest -i "$OUT_DIR/_input.css" -o "$OUT_DIR/_tw.css" "$@"
    ;;

  tailwind-v3)
    require tokens_entry_css "$ENTRY"
    if [ ! -f "$OUT_DIR/_input.css" ]; then
      {
        printf '@import "%s%s";\n' "$REL" "$ENTRY"
        printf '@tailwind base;\n@tailwind components;\n@tailwind utilities;\n'
      } > "$OUT_DIR/_input.css"
    fi
    CONFIG=""
    for candidate in tailwind.config.ts tailwind.config.js tailwind.config.cjs tailwind.config.mjs; do
      [ -f "$candidate" ] && CONFIG="-c $candidate" && break
    done
    # shellcheck disable=SC2086
    $DLX tailwindcss@3 $CONFIG \
      -i "$OUT_DIR/_input.css" \
      -o "$OUT_DIR/_tw.css" \
      --content "$OUT_DIR/**/*.html" "$@"
    ;;

  css-vars|other|"")
    require tokens_css "$TOKENS"
    cp "$TOKENS" "$OUT_DIR/_tokens.css"
    echo "Copied $TOKENS -> $OUT_DIR/_tokens.css"
    echo 'Link it: <link rel="stylesheet" href="./_tokens.css">'
    exit 0
    ;;

  *)
    echo "error: unknown css_framework '$FRAMEWORK'" >&2
    echo "expected one of: tailwind-v4, tailwind-v3, css-vars, other" >&2
    exit 1
    ;;
esac

echo "Built $OUT_DIR/_tw.css — link it: <link rel=\"stylesheet\" href=\"./_tw.css\">"
