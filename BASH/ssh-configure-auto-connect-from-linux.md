# Kali SSH + HTB VPN Startup Cheatsheet

## SSH Server

```bash
sudo apt install openssh-server -y
sudo systemctl enable --now ssh
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

# VPN — HTB

## Import `.ovpn`

```bash
sudo nmcli connection import type openvpn file /home/kali/VPN/htb-vpn.ovpn
```

## Enable Network Autoconnect

```bash
sudo nmcli connection modify "Wired connection 1" connection.autoconnect yes
sudo nmcli connection modify "htb-vpn" connection.autoconnect yes connection.autoconnect-retries 0
```

## Create VPN Startup Service

```bash
sudo nano /etc/systemd/system/htb-vpn.service
```

Paste:

```ini
[Unit]
Description=HTB VPN
After=NetworkManager-wait-online.service
Wants=NetworkManager-wait-online.service

[Service]
Type=oneshot
ExecStart=/usr/bin/nmcli connection up "htb-vpn"
RemainAfterExit=yes
ExecStop=/usr/bin/nmcli connection down "htb-vpn"

[Install]
WantedBy=multi-user.target
```

Save and run:

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
htb-vpn
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
nmcli connection up "htb-vpn"
```

## Disconnect VPN

```bash
nmcli connection down "htb-vpn"
```

## Reboot Test

```bash
sudo reboot
```

After reboot:

```bash
nmcli connection show --active
```

If `htb-vpn` and `tun0` appear, the VPN is connected automatically.
