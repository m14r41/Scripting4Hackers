
# VMware Lab Network Cheat Sheet

## 1. Final network design

Assume you are using only **2 VMware networks**:

| Network    | Type      | Subnet             | Purpose                 |
| ---------- | --------- | ------------------ | ----------------------- |
| Vulnerable | Host-only | `10.10.20.0/24`    | Vulnerable/CTF machines |
| NAT        | NAT       | `192.168.140.0/24` | Internet access         |

### Vulnerable network

```text
Network:       10.10.20.0/24
Mask:          255.255.255.0
DHCP:          10.10.20.1 – 10.10.20.10
Gateway:       None
```

DHCP automatically assigns vulnerable machines addresses from:

```text
10.10.20.1
10.10.20.2
...
10.10.20.10
```

---

# 2. NAT network

```text
Network:       192.168.140.0/24
Mask:          255.255.255.0
NAT Gateway:   192.168.140.2
```

### DHCP pool

```text
192.168.140.132 – 192.168.140.145
```

### Static range

You are manually using:

```text
192.168.140.120 – 192.168.140.131
```

These are **outside the DHCP pool**, so you can manually assign them to specific machines.

Current assignments:

```text
192.168.140.120 → Windows Server
192.168.140.121 → Ubuntu Server
```

Future static machines can use:

```text
192.168.140.122
192.168.140.123
...
192.168.140.131
```

Other machines can simply use DHCP:

```text
192.168.140.132 – 192.168.140.145
```

---

# 3. Windows — Static NAT IP

For a Windows VM that needs a permanent NAT IP:

**Network Connections → Adapter → Properties → IPv4**

Select:

```text
Use the following IP address
```

Example for Windows Server:

```text
IP address:        192.168.140.120
Subnet mask:       255.255.255.0
Default gateway:   192.168.140.2

Preferred DNS:     192.168.140.2
Alternate DNS:     blank
```

Then:

```text
OK → Close
```

Verify:

```cmd
ipconfig
```

Expected:

```text
IPv4 Address:    192.168.140.120
Default Gateway: 192.168.140.2
```

---

# 4. Windows — DHCP NAT

If you want a normal VM to automatically receive a NAT address:

Select:

```text
Obtain an IP address automatically
Obtain DNS server address automatically
```

VMware will give it an address from:

```text
192.168.140.132 – 192.168.140.145
```

---

# 5. Ubuntu Server — Static NAT IP

Ubuntu Server is CLI-only, so use **Netplan**.

Your working interface is:

```text
ens33
```

Your working static configuration is:

```yaml
network:
  version: 2
  ethernets:
    ens33:
      dhcp4: false
      dhcp6: false
      addresses:
        - 192.168.140.121/24
      routes:
        - to: default
          via: 192.168.140.2
      nameservers:
        addresses:
          - 192.168.140.2
```

File:

```text
/etc/netplan/00-installer-config.yaml
```

Edit:

```bash
sudo nano /etc/netplan/00-installer-config.yaml
```

Save:

```text
Ctrl + O
Enter
Ctrl + X
```

Apply:

```bash
sudo netplan apply
```

**No reboot required.**

Verify:

```bash
ip a
```

You should see:

```text
192.168.140.121/24
```

Check gateway:

```bash
ip route
```

Expected:

```text
default via 192.168.140.2 dev ens33
```

Test Internet:

```bash
ping -c 4 8.8.8.8
```

Test DNS:

```bash
ping -c 4 google.com
```

---

# 6. Two NIC VM setup

For machines that need **both Internet and the vulnerable network**, use two VMware adapters.

Example:

```text
VM
├── NIC 1 → Vulnerable / Host-only
│           10.10.20.x
│
└── NIC 2 → NAT
            192.168.140.x
```

### Vulnerable NIC

Example:

```text
IP:       10.10.20.5
Mask:     255.255.255.0
Gateway:  BLANK
```

### NAT NIC

Example:

```text
IP:       192.168.140.120
Mask:     255.255.255.0
Gateway:  192.168.140.2
```

### Critical rule

For a two-NIC machine:

> **Only the NAT interface should normally have the default gateway.**

Don't put:

```text
Default gateway: 10.10.20.1
```

on the vulnerable interface.

---

# 7. Your IP allocation plan

Keep this as your quick reference:

```text
========================================
        VULNERABLE NETWORK
========================================

Subnet:       10.10.20.0/24
DHCP:         10.10.20.1 – 10.10.20.10
Gateway:      None

Use for:
- CTF machines
- Vulnerable VMs
- Pentesting targets
- Isolated lab systems


========================================
             NAT NETWORK
========================================

Subnet:       192.168.140.0/24
Gateway:      192.168.140.2

STATIC:
.120 → Windows Server
.121 → Ubuntu Server
.122 → Future static VM
.123 → Future static VM
...
.131 → Future static VM

DHCP:
.132 – .145 → Other VMs
```

---

# 8. Important concept to remember

Your configuration is **not subnetting**.

You're doing:

```text
Subnet
    ↓
192.168.140.0/24

Inside that subnet:
    ↓
Static IP allocation
192.168.140.120–131

and

DHCP pool
192.168.140.132–145
```

The DHCP pool and manually assigned static IPs **must not overlap**.

---

# 9. Quick troubleshooting

### Windows

```cmd
ipconfig
ipconfig /all
ping 192.168.140.2
ping 8.8.8.8
```

### Ubuntu

```bash
ip a
ip route
ping -c 4 192.168.140.2
ping -c 4 8.8.8.8
ping -c 4 google.com
```

### If Ubuntu suddenly gets `.138` again

Check:

```bash
cat /etc/netplan/*.yaml
```

Make sure you have:

```yaml
dhcp4: false
```

and:

```yaml
addresses:
  - 192.168.140.121/24
```

Then:

```bash
sudo netplan apply
```

---

## Your current working setup

```text
                         WINDOWS HOST
                              │
                 ┌────────────┴────────────┐
                 │                         │
             VMnet Host-only           VMnet NAT
             10.10.20.0/24          192.168.140.0/24
                 │                         │
           DHCP .1-.10                Gateway .2
                 │                         │
          Vulnerable VMs          ┌────────┴────────┐
                                  │                 │
                              Windows            Ubuntu
                              .120                .121
                                  │                 │
                                  └──── Internet ───┘
```

This is a **clean small personal pentesting/CTF lab design** and is easy to expand later.
