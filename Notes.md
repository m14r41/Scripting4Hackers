

# MobSF Docker Setup & Management

```bash
# Stop the running MobSF container (if it exists)
docker stop mobsf

# Remove the existing MobSF container
docker rm mobsf

# Ensure Docker starts automatically on system boot
sudo systemctl enable docker

# Start a new MobSF container with auto-restart enabled
docker run -d --name mobsf --restart=always -p 8182:8000 opensecurity/mobile-security-framework-mobsf

# Remove the MobSF container (Use only if you want to delete it)
docker rm mobsf

