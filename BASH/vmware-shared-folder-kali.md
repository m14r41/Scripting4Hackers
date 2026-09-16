# VMware Shared Folder Setup & Removal — Kali Linux

## Prerequisites

* VMware Workstation
* Kali Linux VM
* VMware Shared Folder configured in:
  `VM → Settings → Options → Shared Folders`
* `open-vm-tools` installed in Kali Linux

### Install Required VMware Tools

```bash
sudo apt update && sudo apt install -y open-vm-tools open-vm-tools-desktop
```

Enable the service:

```bash
sudo systemctl enable --now open-vm-tools
```

Verify:

```bash
systemctl status open-vm-tools --no-pager
```

Check available VMware shared folders:

```bash
vmware-hgfsclient
```

---

## Setup

Define the VMware shared folder name:

```bash
SHARE="Share-with-VMs"
```

Run:

```bash
SHARE="Share-with-VMs"; sudo mkdir -p /mnt/hgfs; vmware-hgfsclient | grep -Fxq "$SHARE" || { echo "Shared folder '$SHARE' not found"; exit 1; }; grep -qE '^\.host:/ /mnt/hgfs fuse\.vmhgfs-fuse ' /etc/fstab || echo '.host:/ /mnt/hgfs fuse.vmhgfs-fuse allow_other,_netdev 0 0' | sudo tee -a /etc/fstab >/dev/null; sudo systemctl daemon-reload; mountpoint -q /mnt/hgfs || sudo mount /mnt/hgfs; rm -f "$HOME/Desktop/$SHARE" "$HOME/$SHARE"; ln -s "/mnt/hgfs/$SHARE" "$HOME/Desktop/$SHARE"; ln -s "/mnt/hgfs/$SHARE" "$HOME/$SHARE"; echo "Setup complete: $SHARE"
```

### Verify

```bash
ls -la /mnt/hgfs/
```

```bash
ls -la "$HOME/Desktop/$SHARE"
```

```bash
ls -la "$HOME/$SHARE"
```

Shared folder location:

```text
/mnt/hgfs/<SHARED_FOLDER>
```

Shortcuts:

```text
~/Desktop/<SHARED_FOLDER>
~/<SHARED_FOLDER>
```

---

## Delete Configuration

Define the shared folder name:

```bash
SHARE="Share-with-VMs"
```

Run:

```bash
SHARE="Share-with-VMs"; rm -f "$HOME/Desktop/$SHARE" "$HOME/$SHARE"; sudo umount /mnt/hgfs 2>/dev/null; sudo sed -i '\|^\.host:/ /mnt/hgfs fuse\.vmhgfs-fuse |d' /etc/fstab; sudo systemctl daemon-reload; echo "Deleted configuration: $SHARE"
```

> This removes the Kali-side mount configuration and shortcuts. It does **not** delete files from the VMware host's shared folder.

---

## Future Shared Folders

Change only the `SHARE` variable:

```bash
SHARE="Projects"
```

or:

```bash
SHARE="Tools"
```

The setup automatically:

1. Checks whether VMware exposes the shared folder.
2. Creates `/mnt/hgfs` if required.
3. Configures automatic mounting.
4. Mounts the VMware shared folders.
5. Creates a Desktop shortcut.
6. Creates a Home-directory shortcut.

### List Available Shared Folders

```bash
vmware-hgfsclient
```

Example:

```text
Share-with-VMs
Projects
Tools
```
