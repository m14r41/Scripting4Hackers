# Kali SSH + HTB VPN Startup Cheatsheet

## SSH Server

Install and enable SSH:

```bash
sudo apt update
sudo apt install openssh-server -y
sudo systemctl enable --now ssh
```

Check:

```bash
systemctl status ssh
```

## Windows — Create SSH Key

```powershell
ssh-keygen -t ed25519
```

## Windows — Copy SSH Key to Kali

```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | ssh kali@192.168.66.169 "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```

## Future SSH Login

```powershell
ssh kali@192.168.66.169
```

---

# HTB VPN

## Import `.ovpn`

```bash
sudo nmcli connection import type openvpn file /home/kali/VPN/htb-vpn.ovpn
```

## Find the VPN Connection Name

Never assume the imported VPN is named `htb-vpn`.

```bash
nmcli connection show
```

Example:

```text
NAME
lab-vpn
Wired connection 1
tun0
lo
```

Set your actual VPN name:

```text
lab-vpn
```

## Configure Normal Internet Routing

Prevent the HTB VPN from becoming the default Internet route:

```bash
sudo nmcli connection modify "lab-vpn" ipv4.never-default yes
```

Result:

```text
Internet → eth0
HTB     → tun0
```

## Disable IPv6

Disable IPv6 on the normal wired connection:

```bash
sudo nmcli connection modify "Wired connection 1" ipv6.method disabled
```

Also disable IPv6 on the HTB VPN:

```bash
sudo nmcli connection modify "lab-vpn" ipv6.method disabled
```

## VPN Autoconnect

Do not enable NetworkManager autoconnect for the VPN when using the systemd startup service:

```bash
sudo nmcli connection modify "lab-vpn" connection.autoconnect no
```

Keep the normal network connection enabled:

```bash
sudo nmcli connection modify "Wired connection 1" connection.autoconnect yes
```

---

# VPN Startup Service

Create:

```bash
sudo nano /etc/systemd/system/htb-vpn.service
```

Use:

```ini
[Unit]
Description=HTB VPN
After=NetworkManager-wait-online.service
Wants=NetworkManager-wait-online.service

[Service]
Type=oneshot
ExecStart=/usr/bin/nmcli connection up "lab-vpn"
ExecStop=/usr/bin/nmcli connection down "lab-vpn"
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable htb-vpn.service
sudo systemctl start htb-vpn.service
```

## Check Active Connections

```bash
nmcli connection show --active
```

Expected:

```text
lab-vpn
Wired connection 1
tun0
lo
```

## Check VPN Service

```bash
systemctl status htb-vpn.service
```

## Manually Connect VPN

```bash
sudo nmcli connection up "lab-vpn"
```

## Disconnect VPN

```bash
sudo nmcli connection down "lab-vpn"
```

---

# Verify Routing

Check:

```bash
ip route
```

Expected:

```text
default via 192.168.66.2 dev eth0

10.10.10.0/23 via 10.10.14.1 dev tun0
10.10.14.0/23 dev tun0
10.129.0.0/16 via 10.10.14.1 dev tun0
```

The important rule is:

```text
Default Internet → eth0
HTB Networks     → tun0
```

## Test Internet

```bash
ping -c 3 google.com
```

Check Internet routing:

```bash
ip route get 8.8.8.8
```

Expected:

```text
dev eth0
```

## Test HTB Routing

```bash
ip route get 10.129.1.1
```

Expected:

```text
dev tun0
```

---

# Reboot Test

```bash
sudo reboot
```

After reboot:

```bash
nmcli connection show --active
```

Check:

```bash
ip route
```

Test Internet:

```bash
ping -c 3 google.com
```

Test HTB:

```bash
ip route get 10.129.1.1
```

If the VPN service is enabled and `tun0` is present, no manual configuration is required after future reboots.

---

# Final Configuration

```text
                    Kali
                      |
                 ┌────┴────┐
                 │         │
               eth0       tun0
                 │         │
          192.168.66.2   10.10.14.1
                 │         │
             Internet      HTB
                            │
                     10.10.10.0/23
                     10.129.0.0/16
```

## Important Rules

1. Always check the imported VPN name with:

```bash
nmcli connection show
```

2. Never assume the VPN name is `htb-vpn`.

3. Set:

```bash
ipv4.never-default yes
```

4. If IPv6 is not required, disable it on both the wired connection and VPN.

5. Use the systemd service for VPN startup instead of enabling VPN autoconnect as a second startup mechanism.

6. After configuration, verify:

```bash
ip route
ping -c 3 google.com
```

The expected behavior is:

```text
Internet → eth0
HTB     → tun0
SSH     → eth0
```
