# Troubleshooting Guide

This guide helps you solve common issues when using the Python Docker Template. Most problems have simple solutions!

## 🚨 Quick Fixes

Before diving into specific issues, try these common solutions:

```bash
# 1. Restart everything
make down
make up

# 2. Rebuild from scratch  
make rebuild

# 3. Nuclear option (removes everything)
make clean
make up
```

## 🐳 Docker Issues

### "docker: command not found"

**Problem**: Docker is not installed or not in PATH

**Solutions**:
1. **Install Docker Desktop**:
   - Windows/Mac: Download from [docker.com](https://www.docker.com/products/docker-desktop/)
   - Linux: Follow [official installation guide](https://docs.docker.com/engine/install/)

2. **Verify installation**:
   ```bash
   docker --version
   docker-compose --version
   ```

3. **Check Docker is running**:
   - Windows/Mac: Look for Docker Desktop in system tray
   - Linux: `sudo systemctl status docker`

### "Permission denied" when running Docker commands

**Problem**: User doesn't have Docker permissions

**Solutions**:

**Windows**:
```bash
# Run PowerShell as Administrator
# Right-click PowerShell -> "Run as Administrator"
```

**Mac/Linux**:
```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Logout and login again, or restart terminal
# Then test:
docker ps
```

**Alternative** (temporary):
```bash
sudo make up
sudo make run FILE=main.py
```

### "Container name already in use"

**Problem**: Container with same name exists

**Solutions**:
```bash
# Remove existing container
docker rm -f python-learning

# Or use make command
make down
make up
```

### "Port already in use" 

**Problem**: Another service is using the same port

**Solutions**:
1. **Find what's using the port**:
   ```bash
   # Windows
   netstat -ano | findstr :8000
   
   # Mac/Linux  
   lsof -i :8000
   ```

2. **Stop the conflicting service** or **change port**:
   ```yaml
   # In docker-compose.yml
   ports:
     - "8001:8000"  # Use different host port
   ```

### "No space left on device"

**Problem**: Docker is using too much disk space

**Solutions**:
```bash
# Clean up Docker resources
make clean

# More aggressive cleanup
docker system prune -a --volumes

# Check disk usage
docker system df
```

## 🔧 Make Command Issues

### "make: command not found"

**Problem**: Make is not installed

**Solutions**:

**Windows (Recommended - WSL)**:
```bash
# Install WSL2 and Ubuntu
wsl --install -d Ubuntu

# Make is pre-installed in WSL Ubuntu
# Just use WSL terminal for all commands
```

**Windows (Alternative)**:
```bash
# Option 1: Chocolatey
choco install make

# Option 2: Scoop
scoop install make

# Option 3: Use Git Bash (comes with Git for Windows)
```

**Mac**:
```bash
# Install Xcode Command Line Tools
xcode-select --install

# Or use Homebrew
brew install make
```

**Linux**:
```bash
# Ubuntu/Debian
sudo apt-get install build-essential

# CentOS/RHEL
sudo yum groupinstall "Development Tools"
```

### "No rule to make target"

**Problem**: Typo in make command or target doesn't exist

**Solutions**:
```bash
# Check available commands
make help

# Common typos:
make run FILE=main.py  # Correct
make run file=main.py  # Wrong - case sensitive
```

### Make commands hang or timeout

**Problem**: Docker container issues or resource constraints

**Solutions**:
1. **Check container status**:
   ```bash
   make status
   docker ps -a
   ```

2. **Restart Docker Desktop** (Windows/Mac)

3. **Free up resources**:
   ```bash
   # Close other applications
   # Check available memory and disk space
   ```

## 🐍 Python Issues

### "ModuleNotFoundError: No module named 'xyz'"

**Problem**: Python package not installed in container

**Solutions**:
1. **Add to requirements.txt**:
   ```txt
   requests==2.31.0
   numpy==1.25.2
   ```

2. **Rebuild container**:
   ```bash
   make rebuild
   ```

3. **Verify installation**:
   ```bash
   make python CMD='-c "import requests; print(\"Success!\")"'
   ```

### "Permission denied" inside container

**Problem**: File permissions issue

**Solutions**:
1. **Check file ownership on host**:
   ```bash
   ls -la
   ```

2. **Fix permissions** (Mac/Linux):
   ```bash
   chmod +x my_script.py
   ```

3. **Rebuild container**:
   ```bash
   make rebuild
   ```

### Python script won't run

**Problem**: Various script issues

**Debugging steps**:
1. **Check syntax**:
   ```bash
   make python CMD='-m py_compile main.py'
   ```

2. **Run with verbose output**:
   ```bash
   make python CMD='-v main.py'
   ```

3. **Check Python version**:
   ```bash
   make python CMD='--version'
   ```

4. **Interactive debugging**:
   ```bash
   make shell
   python main.py
   ```

### "File not found" when running scripts

**Problem**: File path issue or file doesn't exist

**Solutions**:
1. **Check file exists**:
   ```bash
   make shell
   ls -la
   ```

2. **Use correct path**:
   ```bash
   make run FILE=examples/01_variables.py  # Correct
   make run FILE=01_variables.py           # Wrong
   ```

3. **Check current directory**:
   ```bash
   make python CMD='-c "import os; print(os.getcwd())"'
   ```

## 🔗 Network Issues

### "Connection refused" or "Network timeout"

**Problem**: Network connectivity issues

**Solutions**:
1. **Check internet connection**:
   ```bash
   ping google.com
   ```

2. **Test from container**:
   ```bash
   make shell
   ping google.com
   curl https://httpbin.org/json
   ```

3. **Check Docker network**:
   ```bash
   docker network ls
   docker network inspect bridge
   ```

### "DNS resolution failed"

**Problem**: Container can't resolve domain names

**Solutions**:
1. **Restart Docker Desktop**

2. **Configure DNS** in docker-compose.yml:
   ```yaml
   services:
     python-app:
       dns:
         - 8.8.8.8
         - 8.8.4.4
   ```

3. **Check host DNS**:
   ```bash
   nslookup google.com
   ```

## 💾 File and Volume Issues

### "Changes not reflected in container"

**Problem**: Volume mounting not working properly

**Solutions**:
1. **Verify volume mount**:
   ```bash
   docker inspect python-learning | grep -A 10 Mounts
   ```

2. **Restart container**:
   ```bash
   make down
   make up
   ```

3. **Check file in container**:
   ```bash
   make shell
   cat main.py  # Should show your changes
   ```

### "File exists but can't access"

**Problem**: File permissions or ownership

**Solutions**:
1. **Check permissions**:
   ```bash
   ls -la filename.py
   ```

2. **Fix ownership** (Mac/Linux):
   ```bash
   sudo chown $USER:$USER filename.py
   ```

3. **Fix permissions**:
   ```bash
   chmod 644 filename.py
   ```

## 🚀 Performance Issues

### "Container very slow to start"

**Problem**: Resource constraints or Docker configuration

**Solutions**:
1. **Increase Docker resources**:
   - Docker Desktop → Settings → Resources
   - Increase Memory and CPU allocation

2. **Clean up Docker**:
   ```bash
   make clean
   docker system prune
   ```

3. **Check system resources**:
   - Close other applications
   - Free up disk space

### "Python scripts run slowly"

**Problem**: Container resource limits or inefficient code

**Solutions**:
1. **Profile your code**:
   ```bash
   make python CMD='-m cProfile my_script.py'
   ```

2. **Check container resources**:
   ```bash
   docker stats python-learning
   ```

3. **Optimize Docker image**:
   ```dockerfile
   # Use minimal base image
   FROM python:3.11-slim
   ```

## 🔍 Debugging Techniques

### View Container Logs
```bash
make logs
# or
docker logs python-learning
```

### Interactive Debugging
```bash
# Enter container shell
make shell

# Check Python environment
python -c "import sys; print(sys.path)"
python -c "import os; print(os.environ)"

# Test imports
python -c "import requests; print('requests OK')"
```

### Check Container State
```bash
# Container info
docker inspect python-learning

# Resource usage
docker stats python-learning

# Running processes
docker exec python-learning ps aux
```

### Test Network Connectivity
```bash
# From host
ping 8.8.8.8

# From container
make python CMD='-c "import requests; print(requests.get(\"https://httpbin.org/json\").json())"'
```

## 📱 Platform-Specific Issues

### Windows Issues

**WSL2 Backend Problems**:
```bash
# Update WSL2
wsl --update

# Restart WSL2
wsl --shutdown
# Restart Docker Desktop
```

**Path Issues**:
```bash
# Use forward slashes in paths
make run FILE=examples/01_variables.py  # Good
make run FILE=examples\01_variables.py  # Bad
```

### Mac Issues

**M1/M2 Chip Compatibility**:
```dockerfile
# In Dockerfile, use platform-specific image
FROM --platform=linux/amd64 python:3.11-slim
```

**File Permission Issues**:
```bash
# Fix Docker Desktop file sharing
# Docker Desktop → Preferences → Resources → File Sharing
```

### Linux Issues

**SELinux Problems**:
```bash
# Temporarily disable SELinux
sudo setenforce 0

# Or configure SELinux context
sudo chcon -Rt svirt_sandbox_file_t /path/to/project
```

**User Namespace Issues**:
```bash
# Add to docker-compose.yml
services:
  python-app:
    user: "${UID}:${GID}"
```

## 🆘 When All Else Fails

### Complete Reset
```bash
# 1. Stop everything
make down

# 2. Remove all Docker resources
make clean

# 3. Clean Docker system
docker system prune -a --volumes

# 4. Restart Docker Desktop

# 5. Start fresh
make up
```

### Get Help

1. **Check logs first**:
   ```bash
   make logs
   ```

2. **Search for error messages**:
   - Copy exact error message
   - Search on Google or Stack Overflow
   - Check Docker/Python documentation

3. **Create minimal reproduction**:
   - Start with basic example
   - Add complexity gradually
   - Isolate the problem

4. **Ask for help**:
   - Provide exact error messages
   - Include system information
   - Share relevant configuration files

### System Information for Bug Reports
```bash
# Docker version
docker --version
docker-compose --version

# System information
# Windows
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"

# Mac
sw_vers

# Linux
uname -a
lsb_release -a

# Docker system info
docker system info
```

## ✅ Prevention Tips

### Regular Maintenance
```bash
# Weekly cleanup
make clean
docker system prune

# Update base image
docker pull python:3.11-slim
make rebuild
```

### Best Practices
1. **Keep requirements.txt updated**
2. **Use specific package versions**
3. **Regular Docker cleanup**
4. **Monitor system resources**
5. **Backup important work**

### Monitoring
```bash
# Check resource usage
docker stats

# Monitor logs
make logs -f

# Health checks
make status
```

---

**Remember**: Most issues have simple solutions. Start with basic troubleshooting before trying complex fixes!

**Still stuck?** Check the other documentation files or create an issue with your specific problem and system details.