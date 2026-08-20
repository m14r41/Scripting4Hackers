**Fuzzing** — Interactive web content enumeration launcher with:

* **ffuf** — Fast web fuzzer
* **Feroxbuster** — Recursive content discovery
* **Gobuster** — Directory/file brute-forcing
* **Dirsearch** — Web path scanner
* **Wfuzz** — Web application fuzzer
* **Dirb** — Web content scanner

It uses the existing `$ip`, asks for a target only when needed, and runs **one selected tool at a time**.

# for Current shell
```
echo 'allFuzz() { if [ -z "$ip" ]; then read -r "ip?Enter IP/domain: "; export ip; fi; w="/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt"; echo; echo "1) ffuf"; echo "2) feroxbuster"; echo "3) gobuster"; echo "4) dirsearch"; echo "5) wfuzz"; echo "6) dirb"; echo "0) Exit"; read -r "c?Select: "; case "$c" in 1) ffuf -u "http://$ip/FUZZ" -w "$w" -t 100 -o ffuf.txt;; 2) feroxbuster -u "http://$ip" -w "$w" -t 100 -o feroxbuster.txt;; 3) gobuster dir -u "http://$ip" -w "$w" -t 100 -o gobuster.txt;; 4) dirsearch -u "http://$ip" -o dirsearch.txt;; 5) wfuzz -c -w "$w" --hc 404 "http://$ip/FUZZ";; 6) dirb "http://$ip" -o dirb.txt;; 0) return;; *) echo "[!] Invalid selection.";; esac; }' >> ~/.zshrc && source ~/.zshrc
```

# Till system not shut down

```bash
echo 'Fuzzing() { if [ -z "$ip" ] && [ -f /tmp/ctf_ip ]; then export ip=$(cat /tmp/ctf_ip); fi; if [ -z "$ip" ]; then read -r "ip?Enter IP/domain: "; export ip; echo "$ip" > /tmp/ctf_ip; fi; w="/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt"; echo; echo "Target: $ip"; echo "1) ffuf"; echo "2) feroxbuster"; echo "3) gobuster"; echo "4) dirsearch"; echo "5) wfuzz"; echo "6) dirb"; echo "0) Exit"; read -r "c?Select: "; case "$c" in 1) ffuf -u "http://$ip/FUZZ" -w "$w" -t 100 -o ffuf.txt;; 2) feroxbuster -u "http://$ip" -w "$w" -t 100 -o feroxbuster.txt;; 3) gobuster dir -u "http://$ip" -w "$w" -t 100 -o gobuster.txt;; 4) dirsearch -u "http://$ip" -o dirsearch.txt;; 5) wfuzz -c -w "$w" --hc 404 "http://$ip/FUZZ";; 6) dirb "http://$ip" -o dirb.txt;; 0) return;; *) echo "[!] Invalid selection.";; esac; }' >> ~/.zshrc && source ~/.zshrc
```
