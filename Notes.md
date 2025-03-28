

# MobSF Docker Setup & Management

# MobSF Docker Setup & Management

```bash
docker stop mobsf  # Stop the running MobSF container (if it exists)
docker rm mobsf  # Remove the existing MobSF container
sudo systemctl enable docker  # Ensure Docker starts automatically on system boot
docker run -d --name mobsf --restart=always -p 8182:8000 opensecurity/mobile-security-framework-mobsf  # Start a new MobSF container with auto-restart enabled
docker rm mobsf  # Remove the MobSF container (Use only if you want to delete it)


