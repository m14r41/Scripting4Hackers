Set up SSH server on Kali, generate an Ed25519 key on Windows, copy the public key to Kali, and enable passwordless SSH login.

```bash
sudo apt install openssh-server -y
sudo systemctl enable --now ssh
```

```powershell
ssh-keygen -t ed25519
```

```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | ssh kali@192.168.66.169 "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```

```powershell
ssh kali@192.168.66.169
```
