#!/bin/bash

domain=$1

if [ -z "$domain" ]; then
  echo "Usage: $0 domain.com"
  exit 1
fi

outdir="$domain-recon"
mkdir -p "$outdir"

echo "[+] Target: $domain"
echo "[+] Output: $outdir"

# -------------------------
# 1. Subdomain Enumeration (4 tools)
# -------------------------
echo "[+] Running subfinder..."
subfinder -d "$domain" -all -silent > "$outdir/subfinder.txt"

echo "[+] Running amass (passive)..."
amass enum -passive -d "$domain" > "$outdir/amass.txt"

echo "[+] Running assetfinder..."
assetfinder --subs-only "$domain" > "$outdir/assetfinder.txt"

echo "[+] Running findomain..."
findomain -t "$domain" -q > "$outdir/findomain.txt"

# Merge all subdomains
cat "$outdir/"*.txt | sort -u > "$outdir/all_subs.txt"

# -------------------------
# 2. Live host check
# -------------------------
echo "[+] Probing live hosts..."
httpx -l "$outdir/all_subs.txt" -silent -status-code -title -tech-detect > "$outdir/alive.txt"

# -------------------------
# 3. Nuclei scan
# -------------------------
echo "[+] Running nuclei scan..."
nuclei -l "$outdir/alive.txt" \
  -severity medium,high,critical \
  -o "$outdir/nuclei.txt"

# -------------------------
# DONE
# -------------------------
echo "[+] Done!"
echo "[+] Subdomains → $outdir/all_subs.txt"
echo "[+] Alive → $outdir/alive.txt"
echo "[+] Findings → $outdir/nuclei.txt"
