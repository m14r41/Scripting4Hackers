#!/bin/bash

# ============================================================
# Fast Lab Enumeration
# ============================================================

#  Sample Output
#     enum_10.10.10.10/
#     ├── normal.txt
#     ├── full.txt
#     ├── dirb.txt
#     ├── dirsearch.txt
#     └── udp.txt



TARGET="$1"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
DIM='\033[2m'
RESET='\033[0m'

# ------------------------------------------------------------
# Input
# ------------------------------------------------------------

if [ -z "$TARGET" ]; then
    echo -e "${RED}Usage:${RESET} $0 <IP>"
    echo -e "${DIM}Example:${RESET} $0 10.10.10.10"
    exit 1
fi

# ------------------------------------------------------------
# Output
# ------------------------------------------------------------

OUT="enum_${TARGET}"

NORMAL="$OUT/normal.txt"
FULL="$OUT/full.txt"
DIRB="$OUT/dirb.txt"
DIRSEARCH="$OUT/dirsearch.txt"
UDP="$OUT/udp.txt"

mkdir -p "$OUT"

: > "$DIRB"
: > "$DIRSEARCH"

# ------------------------------------------------------------
# Runtime
# ------------------------------------------------------------

WEB_PIDS=()
WEB_STARTED=""

# ------------------------------------------------------------
# Start Web Enumeration
# ------------------------------------------------------------

start_web_enum() {

    local PORT="$1"
    local SCHEME="$2"
    local URL="${SCHEME}://${TARGET}:${PORT}"

    # Prevent duplicate scans
    if echo "$WEB_STARTED" | grep -qw "$PORT"; then
        return
    fi

    WEB_STARTED="$WEB_STARTED $PORT"

    echo
    echo -e "      ${GREEN}Web:${RESET} $URL"
    echo -e "      ${DIM}DIRB      :${RESET} dirb $URL"
    echo -e "      ${DIM}Dirsearch :${RESET} dirsearch -u $URL --quiet-mode"
    echo -e "      ${YELLOW}Status    : Running in background${RESET}"

    # --------------------------------------------------------
    # DIRB
    # --------------------------------------------------------

    {
        echo
        echo "=================================================="
        echo "DIRB TARGET : $URL"
        echo "=================================================="

        dirb "$URL" -S 2>/dev/null

        echo
    } >> "$DIRB" 2>&1 &

    WEB_PIDS+=("$!")

    # --------------------------------------------------------
    # Dirsearch
    # --------------------------------------------------------

    {
        echo
        echo "=================================================="
        echo "DIRSEARCH TARGET : $URL"
        echo "=================================================="

        dirsearch \
            -u "$URL" \
            --format plain \
            --quiet-mode \
            --status-codes 200,204,301,302,307,308,401,403 \
            2>/dev/null

        echo
    } >> "$DIRSEARCH" 2>&1 &

    WEB_PIDS+=("$!")
}

# ------------------------------------------------------------
# Detect OPEN HTTP/HTTPS Services
# ------------------------------------------------------------

detect_web() {

    local FILE="$1"

    while IFS= read -r LINE; do

        # Only process explicitly OPEN TCP ports
        if ! echo "$LINE" | grep -qE '^[0-9]+/tcp[[:space:]]+open[[:space:]]'; then
            continue
        fi

        PORT=$(echo "$LINE" | cut -d'/' -f1)

        # HTTPS
        if echo "$LINE" | grep -qiE 'https|ssl/http'; then
            SCHEME="https"

        # HTTP
        elif echo "$LINE" | grep -qiE 'http|http-proxy'; then
            SCHEME="http"

        else
            continue
        fi

        start_web_enum "$PORT" "$SCHEME"

    done < <(
        awk '
        /^[0-9]+\/tcp[[:space:]]+open[[:space:]]/ {
            if ($0 ~ /http|https|ssl\/http|http-proxy/) {
                print
            }
        }' "$FILE"
    )
}

# ------------------------------------------------------------
# Header
# ------------------------------------------------------------

clear

echo
echo -e "${CYAN}==========================================${RESET}"
echo -e "        ${WHITE}Fast Lab Enumeration${RESET}"
echo -e "${CYAN}==========================================${RESET}"
echo -e "${WHITE}Target :${RESET} ${GREEN}$TARGET${RESET}"
echo -e "${WHITE}Output :${RESET} ${GREEN}$OUT/${RESET}"
echo

# ============================================================
# 1. Basic Nmap
# ============================================================

echo -e "${CYAN}[1/4]${RESET} ${WHITE}Basic Nmap scan${RESET}"
echo -e "      ${DIM}Command :${RESET} nmap $TARGET"
echo -e "      ${DIM}Output  :${RESET} $NORMAL"
echo -e "      ${YELLOW}Status  : Running...${RESET}"

nmap "$TARGET" -oN "$NORMAL"

if [ $? -ne 0 ]; then
    echo -e "      ${RED}Status  : Failed${RESET}"
    exit 1
fi

echo -e "      ${GREEN}Status  : Completed${RESET}"

# ============================================================
# Detect Web From Basic Scan
# ============================================================

echo
echo -e "      ${WHITE}Checking basic scan for web services...${RESET}"

BASIC_WEB=$(awk '
/^[0-9]+\/tcp[[:space:]]+open[[:space:]]/ {
    if ($0 ~ /http|https|ssl\/http|http-proxy/) {
        print
    }
}' "$NORMAL")

if [ -n "$BASIC_WEB" ]; then

    echo -e "      ${GREEN}[+] Web service detected${RESET}"
    echo -e "      ${YELLOW}[*] Starting DIRB + Dirsearch in background${RESET}"

    detect_web "$NORMAL"

else

    echo -e "      ${DIM}[-] No web service detected${RESET}"

fi

# ============================================================
# 2. Full TCP
# ============================================================

echo
echo -e "${CYAN}[2/4]${RESET} ${WHITE}Full TCP enumeration${RESET}"
echo -e "      ${DIM}Command :${RESET} nmap -p- -sC -sV -A $TARGET"
echo -e "      ${DIM}Output  :${RESET} $FULL"

if [ ${#WEB_PIDS[@]} -gt 0 ]; then
    echo -e "      ${YELLOW}Status  : Running alongside web enumeration...${RESET}"
else
    echo -e "      ${YELLOW}Status  : Running...${RESET}"
fi

nmap -p- -sC -sV -A "$TARGET" -oN "$FULL"

if [ $? -ne 0 ]; then
    echo -e "      ${RED}Status  : Failed${RESET}"
else
    echo -e "      ${GREEN}Status  : Completed${RESET}"
fi

# ============================================================
# Detect Additional Web Services
# ============================================================

echo
echo -e "      ${WHITE}Checking full scan for additional web services...${RESET}"

OLD_WEB_STARTED="$WEB_STARTED"

detect_web "$FULL"

if [ "$OLD_WEB_STARTED" = "$WEB_STARTED" ]; then

    if [ -n "$WEB_STARTED" ]; then
        echo -e "      ${DIM}[-] No additional web services found${RESET}"
    else
        echo -e "      ${DIM}[-] No web services detected${RESET}"
    fi

else

    echo -e "      ${GREEN}[+] Additional web service detected${RESET}"
    echo -e "      ${YELLOW}[*] DIRB + Dirsearch started in background${RESET}"

fi

# ============================================================
# Wait For Web Enumeration
# ============================================================

if [ ${#WEB_PIDS[@]} -gt 0 ]; then

    echo
    echo -e "      ${YELLOW}[*] Waiting for web enumeration...${RESET}"

    for PID in "${WEB_PIDS[@]}"; do
        wait "$PID"
    done

    echo -e "      ${GREEN}[+] Web enumeration completed${RESET}"

else

    echo "No HTTP/HTTPS services detected." > "$DIRB"
    echo "No HTTP/HTTPS services detected." > "$DIRSEARCH"

fi

# ============================================================
# 3. UDP
# ============================================================

echo
echo -e "${CYAN}[3/4]${RESET} ${WHITE}UDP scan${RESET}"
echo -e "      ${DIM}Command :${RESET} nmap -sU --min-rate 5000 $TARGET"
echo -e "      ${DIM}Output  :${RESET} $UDP"
echo -e "      ${YELLOW}Status  : Running at 5000 packets/sec...${RESET}"

nmap -sU --min-rate 5000 "$TARGET" -oN "$UDP"

if [ $? -eq 0 ]; then
    echo -e "      ${GREEN}Status  : Completed${RESET}"
else
    echo -e "      ${RED}Status  : Failed${RESET}"
fi

# ============================================================
# 4. Summary
# ============================================================

echo
echo -e "${CYAN}[4/4]${RESET} ${WHITE}Enumeration complete${RESET}"

echo
echo -e "${CYAN}==========================================${RESET}"
echo -e "        ${GREEN}Results${RESET}"
echo -e "${CYAN}==========================================${RESET}"

echo -e "  ${GREEN}Normal${RESET}     → $NORMAL"
echo -e "  ${GREEN}Full TCP${RESET}   → $FULL"
echo -e "  ${GREEN}DIRB${RESET}       → $DIRB"
echo -e "  ${GREEN}Dirsearch${RESET}  → $DIRSEARCH"
echo -e "  ${GREEN}UDP${RESET}        → $UDP"

echo
echo -e "${GREEN}Done.${RESET}"
echo
