# Getting Started Guide

This guide will help you set up and start using the Python Docker Template in just a few minutes.

## 📋 Prerequisites

Before you begin, make sure you have the following installed on your system:

### Required Software

1. **Docker Desktop** (Windows/Mac) or **Docker Engine** (Linux)
   - Download from: https://www.docker.com/products/docker-desktop/
   - Verify installation: `docker --version`

2. **Docker Compose** (usually included with Docker Desktop)
   - Verify installation: `docker-compose --version`

3. **Make** (for using the Makefile)
   - **Windows** (recommended): Use WSL (Windows Subsystem for Linux) - see WSL setup below
   - **Windows** (alternative): Install via Chocolatey: `choco install make` or use Git Bash
   - **Mac**: Usually pre-installed, or `brew install make`
   - **Linux**: Usually pre-installed, or `sudo apt install make`

4. **Git** (optional, for version control)
   - Download from: https://git-scm.com/downloads

### WSL Setup for Windows (Recommended)

For the best experience on Windows, we recommend using WSL (Windows Subsystem for Linux):

1. **Install WSL2**:
   ```bash
   # Run in PowerShell as Administrator
   wsl --install
   ```

2. **Install Ubuntu** (or your preferred Linux distribution):
   ```bash
   wsl --install -d Ubuntu
   ```

3. **Restart your computer** when prompted

4. **Open WSL terminal** and install Docker:
   ```bash
   # Update package list
   sudo apt update
   
   # Install Docker
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   
   # Add your user to docker group
   sudo usermod -aG docker $USER
   ```

5. **Install Docker Desktop** for Windows and enable WSL2 integration

6. **Clone this repository in WSL**:
   ```bash
   cd ~
   git clone <your-repo-url>
   cd python-docker-template
   ```

**Why WSL?**
- ✅ Native Linux environment with full Makefile support
- ✅ Better Docker performance and compatibility
- ✅ Same commands work as on Linux/Mac
- ✅ No need to install Make separately
- ✅ Better file permissions handling

### System Requirements
- At least 2GB of free disk space
- 4GB RAM (8GB recommended)
- Internet connection (for initial setup)

## 🚀 Quick Start (5 Minutes)

### Step 1: Get the Template
```bash
# Clone the repository
git clone <your-repo-url>
cd python-docker-template

# Or download and extract the ZIP file
```

### Step 2: Build and Start
```bash
# Build the Docker image and start the container
make up
```

This command will:
- Build the Docker image with Python 3.11
- Install all packages from `requirements.txt`
- Start the container in the background

### Step 3: Run Your First Python Program
```bash
# Run the main.py file
make run FILE=main.py
```

You should see output like this:
```
🐍 Welcome to Python Learning with Docker! 🐳
==================================================
...
✅ Great job! You've completed the basic examples.
```

### Step 4: Try the Examples
```bash
# Run the variable examples
make run FILE=examples/01_variables.py

# Run the control flow examples  
make run FILE=examples/02_control_flow.py
```

## 🔧 Essential Commands

Once you have everything running, here are the most important commands:

```bash
# Start the environment
make up

# Run any Python file
make run FILE=filename.py

# Run Python commands directly
make python CMD='-c "print(\"Hello World!\")"'

# Open interactive Python shell in container
make shell
# Then type: python

# Stop the environment
make down

# Rebuild after changes (new libraries, etc.)
make rebuild

# View all available commands
make help
```

## 📁 Understanding the Structure

After setup, your project should look like this:

```
python-docker-template/
├── main.py              # ← Your main Python file (start here!)
├── examples/            # ← Learning examples
│   ├── 01_variables.py
│   ├── 02_control_flow.py
│   ├── 03_functions.py
│   ├── 04_file_handling.py
│   └── 05_libraries.py
├── requirements.txt     # ← Python packages (add new ones here)
├── Dockerfile          # ← Container definition
├── docker-compose.yml  # ← Container configuration
├── Makefile            # ← Automation commands
└── docs/               # ← Documentation (guides and help)
```

## ✏️ Your First Modification

Let's modify the main.py file to make it your own:

### Step 1: Edit main.py
Open `main.py` in your favorite text editor and find this line:
```python
name = "Python Learner"
```

Change it to your name:
```python
name = "Your Name Here"
```

### Step 2: Run Your Changes
```bash
make run FILE=main.py
```

You should see your name in the output!

## 📚 Next Steps

### For Python Learning:
1. **Work through examples**: Start with `examples/01_variables.py`
2. **Read the Python guide**: `docs/python-guide.md`
3. **Practice**: Modify the examples and create your own files

### For Understanding Docker:
1. **Read the Docker guide**: `docs/docker-guide.md`
2. **Learn about containers**: `docs/docker-compose-guide.md`
3. **Understand automation**: `docs/makefile-guide.md`

### For Development:
1. **Learn the workflow**: `docs/development-workflow.md`
2. **Add libraries**: `docs/library-management.md`
3. **Follow best practices**: `docs/best-practices.md`

## ❓ Common First-Time Issues

### Problem: "make: command not found"
**Solution**: Install Make for your operating system (see Prerequisites above)

### Problem: "docker: command not found"
**Solution**: Install Docker Desktop and make sure it's running

### Problem: "Container fails to build"
**Solutions**:
1. Check internet connection
2. Try: `make clean` then `make up`
3. Check Docker Desktop is running

### Problem: "Permission denied" errors
**Solutions**:
- **Windows**: Run terminal as Administrator
- **Mac/Linux**: Try `sudo make up` or fix Docker permissions

### Problem: Files not updating in container
**Solution**: The container uses volume mounting, so changes should appear automatically. If not, try `make rebuild`.

## 🎯 Success Checklist

After following this guide, you should be able to:

- ✅ Run `make up` without errors
- ✅ Execute `make run FILE=main.py` and see output
- ✅ Edit `main.py` and see your changes when you run it again
- ✅ Run at least one example file successfully
- ✅ Use `make shell` to access the container

If you can do all of these, you're ready to start learning Python with Docker! 🎉

## 🆘 Need Help?

- Check [Troubleshooting Guide](troubleshooting.md)
- Review the specific component guides in the `docs/` folder
- Look at the examples for practical code samples