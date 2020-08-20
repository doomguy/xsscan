#!/usr/bin/env bash
# Remeber to use: https://www.shellcheck.net
set -euo pipefail
IFS=$'\n\t'

# Uncomment for Debugging
#set -x

echo "[*] Scanning: $TARGET"

for f in lib/*.lst; do
  [[ -e "$f" ]] || break
  ./xsscan.py "$f" "$TARGET" | uniq -c
done

echo "[*] All done. Exiting.."
