# WSL Setup Guide for Windows Users 🪟➡️🐧

This guide provides the best way to use the Python Docker Template on Windows by leveraging Windows Subsystem for Linux (WSL).

## 🎯 Why WSL?

WSL provides a native Linux environment on Windows, which offers:

- ✅ **Native Make support** - No need to install Make separately
- ✅ **Better Docker performance** - Faster container operations
- ✅ **Consistent commands** - Same commands as Linux/Mac documentation
- ✅ **Proper file permissions** - Better handling of Linux-style permissions
- ✅ **Faster file operations** - Improved I/O performance for containers

## 🚀 Quick WSL Setup

### 1. Install WSL2

Open PowerShell as Administrator and run:

```powershell
wsl --install
```

Or install a specific distribution:

```powershell
wsl --install -d Ubuntu
```

### 2. Restart Your Computer

After installation, restart your computer to complete the setup.

### 3. Set Up Your WSL Environment

Open the WSL terminal (search for "Ubuntu" in Start menu) and run:

```bash
# Update package list
sudo apt update && sudo apt upgrade -y

# Install essential tools (Make is already included!)
sudo apt install git curl -y
```

### 4. Install Docker in WSL

```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add your user to docker group
sudo usermod -aG docker $USER

# Reload group membership
newgrp docker
```

### 5. Install Docker Desktop for Windows

1. Download and install [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)
2. During setup, ensure "Use WSL 2 based engine" is checked
3. Go to Settings → Resources → WSL Integration
4. Enable integration with your WSL distribution (Ubuntu)

### 6. Clone and Use the Project

```bash
# Navigate to your home directory
cd ~

# Clone the project
git clone <your-repo-url>
cd python-docker-template

# Start using the Makefile commands!
make up
make run FILE=main.py
```

## 📋 Updated Workflow for Windows

Instead of using PowerShell or Command Prompt, use the WSL terminal for all commands:

```bash
# WSL Terminal (Recommended)
make up              # ✅ Works perfectly
make run FILE=main.py  # ✅ Fast and reliable
make shell           # ✅ Native Linux experience

# PowerShell (Alternative)
make up              # ⚠️ May have performance issues
make run FILE=main.py  # ⚠️ Slower file operations
```

## 🔧 VS Code Integration

For the best development experience, install the WSL extension for VS Code:

1. Install [VS Code](https://code.visualstudio.com/)
2. Install the "WSL" extension
3. Open your project in WSL:

```bash
# In WSL terminal, navigate to your project
cd ~/python-docker-template

# Open in VS Code
code .
```

This gives you:
- Full IntelliSense support
- Integrated terminal that runs in WSL
- Seamless file editing between Windows and WSL
- Docker integration through WSL

## 🛠️ Troubleshooting WSL

### WSL Not Installing
```powershell
# Enable WSL feature manually
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

# Enable Virtual Machine Platform
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# Restart and try again
wsl --install
```

### Docker Not Working in WSL
```bash
# Check if Docker service is running
sudo service docker start

# Test Docker
docker --version
docker ps
```

### Performance Issues
- Store your project files in the WSL filesystem (`/home/username/`) rather than Windows filesystem (`/mnt/c/`)
- This provides much better I/O performance for Docker operations

## 📚 Additional Resources

- [Microsoft WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- [Docker Desktop WSL 2 Backend](https://docs.docker.com/desktop/wsl/)
- [VS Code WSL Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)

## ✨ Benefits Summary

After setting up WSL, you'll enjoy:

| Feature | Windows Native | WSL2 |
|---------|---------------|------|
| Make Commands | ❌ Need to install | ✅ Built-in |
| Docker Performance | ⚠️ Slower | ✅ Fast |
| File Operations | ⚠️ Slower | ✅ Native speed |
| Command Compatibility | ⚠️ Some differences | ✅ Same as Linux |
| Development Experience | ⚠️ Good | ✅ Excellent |

**Ready to get started? Follow the setup steps above and enjoy a superior Python development experience on Windows!** 🚀