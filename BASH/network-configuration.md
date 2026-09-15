
# VMware & Enterprise Networking Cheat Sheet

## 1. Small VMware Lab Network

A simple cybersecurity lab can use two isolated networks:

| Network    | Type      | Subnet             | Purpose                   |
| ---------- | --------- | ------------------ | ------------------------- |
| Vulnerable | Host-only | `10.50.20.0/24`    | CTF / vulnerable machines |
| NAT        | NAT       | `192.168.150.0/24` | Internet access           |

---

## 2. Vulnerable Network

```text
Network:       10.50.20.0/24
Subnet Mask:   255.255.255.0
DHCP:          10.50.20.1 – 10.50.20.10
Gateway:       None
```

DHCP automatically assigns addresses:

```text
10.50.20.1
10.50.20.2
10.50.20.3
...
10.50.20.10
```

Typical uses:

* CTF machines
* Vulnerable VMs
* Deliberately vulnerable applications
* Isolated pentesting targets

---

# 3. NAT Network

```text
Network:       192.168.150.0/24
Subnet Mask:   255.255.255.0
NAT Gateway:   192.168.150.2
```

### Static range

```text
192.168.150.120 – 192.168.150.131
```

Example:

```text
192.168.150.120 → Windows Server
192.168.150.121 → Ubuntu Server
192.168.150.122 → Static VM
192.168.150.123 → Static VM
...
192.168.150.131 → Static VM
```

### DHCP range

```text
192.168.150.132 – 192.168.150.145
```

Other VMs can receive addresses automatically from the DHCP pool.

### Important rule

Static addresses and the DHCP pool **must not overlap**.

```text
STATIC                  DHCP
──────                  ────
.120                    .132
.121                    .133
.122                    .134
.123                    .135
...                     ...
.131                    .145
```

---

# 4. Windows — Static IP

Navigate to:

**Network Connections → Adapter → Properties → IPv4**

Select:

```text
Use the following IP address
```

Example:

```text
IP address:        192.168.150.120
Subnet mask:       255.255.255.0
Default gateway:   192.168.150.2

Preferred DNS:     192.168.150.2
Alternate DNS:     blank
```

Verify:

```cmd
ipconfig
```

---

# 5. Windows — DHCP

For automatic addressing:

```text
Obtain an IP address automatically
Obtain DNS server address automatically
```

The VMware DHCP server assigns an address from its configured pool.

---

# 6. Ubuntu Server — Static IP

Ubuntu Server commonly uses **Netplan**.

Example interface:

```text
ens33
```

Example Netplan configuration:

```yaml
network:
  version: 2
  ethernets:
    ens33:
      dhcp4: false
      dhcp6: false
      addresses:
        - 192.168.150.121/24
      routes:
        - to: default
          via: 192.168.150.2
      nameservers:
        addresses:
          - 192.168.150.2
```

Typical configuration file:

```text
/etc/netplan/00-installer-config.yaml
```

Edit:

```bash
sudo nano /etc/netplan/00-installer-config.yaml
```

Apply:

```bash
sudo netplan apply
```

A reboot is normally **not required**.

Verify:

```bash
ip a
ip route
```

Expected:

```text
192.168.150.121/24
```

and:

```text
default via 192.168.150.2 dev ens33
```

Connectivity tests:

```bash
ping -c 4 192.168.150.2
ping -c 4 8.8.8.8
ping -c 4 google.com
```

---

# 7. Two-NIC VM

A VM that requires both an isolated lab network and Internet can use two network adapters:

```text
                    VM
                     │
             ┌───────┴───────┐
             │               │
           NIC 1           NIC 2
             │               │
        Host-only            NAT
             │               │
        10.50.20.x       192.168.150.x
```

### Isolated/Lab NIC

```text
IP:       10.50.20.5
Mask:     255.255.255.0
Gateway:  blank
```

### NAT NIC

```text
IP:       192.168.150.120
Mask:     255.255.255.0
Gateway:  192.168.150.2
```

### Routing rule

Normally, only the interface connected to the Internet-facing/NAT network should have a **default gateway**.

---

# 8. IP Allocation Design

A simple lab can separate static and dynamic addresses:

```text
========================================
       VULNERABLE NETWORK
========================================

Subnet:       10.50.20.0/24
DHCP:         10.50.20.1 – 10.50.20.10
Gateway:      None


========================================
             NAT NETWORK
========================================

Subnet:       192.168.150.0/24
Gateway:      192.168.150.2

STATIC:
.120 – .131

DHCP:
.132 – .145
```

---

# 9. What Is Subnetting?

**Subnetting** means dividing a larger IP network into smaller networks.

Example:

```text
10.50.0.0/16
```

can be divided into:

```text
10.50.10.0/24
10.50.20.0/24
10.50.30.0/24
10.50.40.0/24
```

Each subnet represents a separate IP network.

---

# 10. Realistic Enterprise Network

A company with approximately 100–200 devices might segment the environment using VLANs and different subnets:

| VLAN | Network    | Subnet          | Typical Use                  |
| ---: | ---------- | --------------- | ---------------------------- |
|   10 | Corporate  | `10.60.10.0/24` | Employee devices             |
|   20 | Servers    | `10.60.20.0/27` | AD, DNS, application servers |
|   30 | Security   | `10.60.30.0/27` | Pentest/security systems     |
|   40 | CTF/Lab    | `10.60.40.0/26` | Security testing             |
|   50 | Management | `10.60.50.0/28` | Network infrastructure       |
|   60 | Guest      | `10.60.60.0/26` | Guest Wi-Fi                  |
|   70 | IoT        | `10.60.70.0/27` | IoT devices                  |

This combines:

**VLANs + subnetting + routing + firewall/ACL policies.**

---

# 11. Common Subnet Sizes

| CIDR  | Subnet Mask       | Total IPs | Traditional Usable Hosts |
| ----- | ----------------- | --------: | -----------------------: |
| `/24` | `255.255.255.0`   |       256 |                      254 |
| `/25` | `255.255.255.128` |       128 |                      126 |
| `/26` | `255.255.255.192` |        64 |                       62 |
| `/27` | `255.255.255.224` |        32 |                       30 |
| `/28` | `255.255.255.240` |        16 |                       14 |
| `/29` | `255.255.255.248` |         8 |                        6 |
| `/30` | `255.255.255.252` |         4 |                        2 |

---

# 12. `/24` → `/26` Subnetting Example

Starting network:

```text
192.168.50.0/24
```

Divide it into four `/26` networks:

```text
192.168.50.0/26
192.168.50.64/26
192.168.50.128/26
192.168.50.192/26
```

### Subnet 1

```text
Network:    192.168.50.0
Usable:     192.168.50.1 – 62
Broadcast:  192.168.50.63
```

### Subnet 2

```text
Network:    192.168.50.64
Usable:     192.168.50.65 – 126
Broadcast:  192.168.50.127
```

### Subnet 3

```text
Network:    192.168.50.128
Usable:     192.168.50.129 – 190
Broadcast:  192.168.50.191
```

### Subnet 4

```text
Network:    192.168.50.192
Usable:     192.168.50.193 – 254
Broadcast:  192.168.50.255
```

---

# 13. Subnetting vs DHCP vs Static IP

These are different concepts:

```text
SUBNETTING
    ↓
Divides networks

Example:
10.60.10.0/24
10.60.20.0/24
10.60.30.0/24
```

```text
DHCP
    ↓
Automatically assigns IP addresses

Example:
10.60.20.100 – 10.60.20.200
```

```text
STATIC IP
    ↓
Manually assigns a fixed IP

Example:
10.60.20.10 → AD Server
```

All three can be used together.

---

# 14. Enterprise Segmentation Example

```text
                         INTERNET
                             │
                         FIREWALL
                             │
                       CORE ROUTER
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
       VLAN 10            VLAN 20            VLAN 30
      Corporate           Servers            Security
    10.60.10.0/24      10.60.20.0/27      10.60.30.0/27
          │                  │                  │
       Laptops             AD/DNS             Kali
       Desktops            Fileserver          Burp
       Printers            Applications        Security VMs
          │                  │                  │
          └──────────── Firewall ACLs ──────────┘
                             │
                          VLAN 40
                         CTF / LAB
                       10.60.40.0/26
                             │
                       Vulnerable VMs
```

Example security policy:

```text
Corporate → Internet       ALLOW
Corporate → Servers        LIMITED
Corporate → CTF            DENY

Security → CTF             ALLOW
Security → Servers         LIMITED
Security → Internet        ALLOW

CTF → Corporate            DENY
CTF → Servers              DENY
```

---

# 15. Private IPv4 Address Ranges

RFC 1918 private address space:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

Examples:

```text
10.60.20.0/24
172.20.50.0/24
192.168.150.0/24
```

These ranges are intended for private/internal networks.

---

# 16. Networking Commands

### Windows

```cmd
ipconfig
ipconfig /all
ipconfig /release
ipconfig /renew
ping 192.168.150.2
tracert 8.8.8.8
route print
nslookup google.com
```

### Linux

```bash
ip a
ip route
ip neigh
ping -c 4 192.168.150.2
ping -c 4 8.8.8.8
traceroute 8.8.8.8
ss -tulpn
resolvectl status
```

---

# 17. Basic Network Troubleshooting

Check in this order:

```text
1. NIC connected?
        ↓
2. Correct VMware network?
        ↓
3. Correct IP address?
        ↓
4. Correct subnet mask?
        ↓
5. Correct default gateway?
        ↓
6. DNS working?
        ↓
7. Firewall / ACL?
        ↓
8. Destination reachable?
```

---

# 18. Quick Reference

```text
STATIC IP
Manual, fixed address

DHCP
Automatic address assignment

DHCP POOL
Range of addresses DHCP can distribute

SUBNET
A logical IP network

SUBNETTING
Dividing a larger network into smaller networks

VLAN
Logical Layer-2 network segmentation

DEFAULT GATEWAY
Router used to reach another network

NAT
Translates private VM traffic through another network/interface

CIDR
Notation such as /24, /26, /27

BROADCAST
Special address used to communicate with all hosts in a subnet
```

### Core concept

```text
Subnetting
    ↓
Creates separate networks

VLANs
    ↓
Separates Layer-2 traffic

DHCP
    ↓
Automatically assigns addresses

Static IP
    ↓
Keeps a device at a manually assigned address

Routing
    ↓
Connects different networks

Firewall / ACL
    ↓
Controls communication between networks
```

