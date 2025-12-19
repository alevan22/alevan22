#!/usr/bin/env bash
set -euo pipefail

# Authorized recon helper (defensive).
# Runs service discovery + version detection + default safe scripts.
#
# Usage:
#   bash scripts/recon_nmap.sh <target> [outdir]
#
# Examples:
#   bash scripts/recon_nmap.sh 192.168.56.200 artifacts/nmap

TARGET="${1:-}"
OUTDIR="${2:-artifacts/nmap}"

if [[ -z "${TARGET}" ]]; then
  echo "Usage: $0 <target> [outdir]" >&2
  exit 1
fi

mkdir -p "${OUTDIR}"

echo "[+] Running Nmap service discovery against: ${TARGET}"
nmap -Pn -n --top-ports 1000 -sS -sV -sC \
  -oA "${OUTDIR}/scan" \
  "${TARGET}"

echo "[+] Outputs:"
echo "    - ${OUTDIR}/scan.nmap (human-readable)"
echo "    - ${OUTDIR}/scan.xml  (machine-readable)"
echo "    - ${OUTDIR}/scan.gnmap (grepable)"
