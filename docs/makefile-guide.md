# Makefile Guide

The Makefile in this template automates common Docker and Python tasks, making development simple and efficient. No need to remember complex commands!

## 🔧 What is a Makefile?

A Makefile is a build automation tool that:
- Defines **targets** (commands you can run)
- Specifies **dependencies** (what needs to happen first)
- Automates **repetitive tasks** with simple commands
- Provides **consistent workflows** across different systems

Instead of typing long Docker commands, you type short make commands!

## 🪟 Windows Users: Use WSL for Best Experience

**Recommended Setup for Windows:**
1. Install WSL2: `wsl --install -d Ubuntu`
2. Use WSL terminal for all make commands
3. Clone project in WSL filesystem (`~/python-docker-template`)

**Why WSL over native Windows?**
- ✅ Native Make support (no additional installation needed)
- ✅ Better Docker performance and file watching
- ✅ Same commands as Linux/Mac documentation
- ✅ Proper file permissions and line endings
- ✅ Faster container startup and file operations

## 📋 Available Commands

Run `make help` to see all available commands:

```bash
make help
```

### Environment Management

```bash
make up          # Start the Docker container
make down        # Stop and remove the container  
make rebuild     # Stop, rebuild and start the container
make status      # Show container status
make logs        # Show container logs
make clean       # Remove all containers and images
```

### Running Python Code

```bash
make run FILE=filename.py           # Run a specific Python file
make python CMD='-c "print(42)"'    # Run Python commands directly
make shell                          # Open interactive shell in container
```

### Development Workflow

```bash
make build       # Build the Docker image
make install     # Rebuild container after adding new requirements
```

## 🔍 Command Details

### `make up`
**What it does:**
- Builds Docker image (if not exists)
- Starts container in background (detached mode)
- Mounts your code directory as volume
- Keeps container running for development

**Equivalent Docker commands:**
```bash
docker-compose up -d
```

**When to use:**
- Starting your development session
- After making changes to docker-compose.yml
- When container is not running

### `make down`
**What it does:**
- Stops the running container
- Removes the container (but keeps the image)
- Cleans up network resources

**Equivalent Docker commands:**
```bash
docker-compose down
```

**When to use:**
- Ending your development session
- Before making changes to Dockerfile
- When you need to free up resources

### `make run FILE=filename.py`
**What it does:**
- Executes a Python file inside the container
- Shows output in your terminal
- Uses the container's Python environment

**Example:**
```bash
make run FILE=main.py
make run FILE=examples/01_variables.py
```

**Equivalent Docker commands:**
```bash
docker exec -it python-learning python filename.py
```

**When to use:**
- Running your Python scripts
- Testing code changes
- Executing example files

### `make python CMD='command'`
**What it does:**
- Runs any Python command inside container
- Useful for quick tests and one-liners

**Examples:**
```bash
make python CMD='-c "print(2+2)"'
make python CMD='--version'
make python CMD='-c "import sys; print(sys.path)"'
```

**When to use:**
- Quick Python calculations
- Testing imports
- Checking Python configuration

### `make shell`
**What it does:**
- Opens an interactive bash shell inside the container
- Allows you to run multiple commands
- Access to full container environment

**Example session:**
```bash
$ make shell
app@container:/app$ python
>>> print("Hello from inside container!")
Hello from inside container!
>>> exit()
app@container:/app$ ls
main.py  examples/  requirements.txt  ...
app@container:/app$ exit
```

**When to use:**
- Interactive development
- Debugging issues
- Exploring the container environment
- Installing packages temporarily

### `make rebuild`
**What it does:**
- Stops current container
- Rebuilds Docker image with latest changes
- Starts new container
- Preserves your code (volume mounted)

**When to use:**
- After modifying requirements.txt
- After changing Dockerfile
- When container behaves unexpectedly
- Installing new Python packages

### `make install`
**What it does:**
- Same as `make rebuild`
- Specifically for adding new Python packages

**Workflow:**
1. Add package to requirements.txt
2. Run `make install`
3. Use new package in your code

### `make build`
**What it does:**
- Builds Docker image from Dockerfile
- Doesn't start container
- Updates image with latest changes

**When to use:**
- After modifying Dockerfile
- Before distributing your project
- Preparing for deployment

### `make status`
**What it does:**
- Shows if container is running
- Displays container information
- Helps diagnose issues

**Example output:**
```bash
CONTAINER ID   IMAGE             COMMAND               STATUS
a1b2c3d4e5f6   python-learning   "tail -f /dev/null"   Up 2 hours
```

### `make logs`
**What it does:**
- Shows container output and error messages
- Useful for debugging
- Displays recent activity

**When to use:**
- Debugging container issues
- Checking startup messages
- Monitoring background processes

### `make clean`
**What it does:**
- Removes all containers and images
- Frees up disk space
- Nuclear option for cleanup

**⚠️ Warning:** This removes everything Docker-related!

**When to use:**
- Freeing up disk space
- Resolving persistent Docker issues
- Starting completely fresh

## 🛠️ How the Makefile Works

### Variables
```makefile
CONTAINER_NAME = python-learning
PYTHON_CMD = docker exec -it $(CONTAINER_NAME) python
```

These define reusable values used throughout the Makefile.

### Targets and Dependencies
```makefile
.PHONY: rebuild
rebuild: down build up
	@echo "Container rebuilt and restarted!"
```

This target:
- Runs `down`, then `build`, then `up` (in that order)
- Prints a message when complete
- `.PHONY` tells make it's not a file target

### Conditional Logic
```makefile
.PHONY: run
run:
	@if [ -z "$(FILE)" ]; then \
		echo "Usage: make run FILE=<filename>"; \
		echo "Example: make run FILE=main.py"; \
	else \
		$(PYTHON_CMD) $(FILE); \
	fi
```

This checks if FILE parameter is provided and gives helpful error messages.

## 🔄 Common Workflows

### Starting Development
```bash
# 1. Start environment
make up

# 2. Verify it's working
make run FILE=main.py

# 3. Start coding!
```

### Adding New Library
```bash
# 1. Edit requirements.txt
echo "requests==2.31.0" >> requirements.txt

# 2. Rebuild with new library
make install

# 3. Use in your code
make run FILE=my_script.py
```

### Daily Development
```bash
# Start session
make up

# Run your code
make run FILE=my_project.py

# Quick Python tests
make python CMD='-c "import requests; print(requests.__version__)"'

# End session
make down
```

### Debugging Issues
```bash
# Check container status
make status

# View logs
make logs

# Interactive debugging
make shell

# Nuclear option
make clean
make up
```

## 🐛 Troubleshooting Make Commands

### "make: command not found"
**Problem:** Make is not installed
**Solutions:**
- Windows: `choco install make` or use Git Bash
- Mac: `brew install make`
- Linux: `sudo apt install make`

### "No rule to make target"
**Problem:** Typo in command or target doesn't exist
**Solution:** Run `make help` to see available commands

### "Container not found" during make commands
**Problem:** Container isn't running
**Solution:** Run `make up` first

### Commands hang or don't respond
**Problem:** Docker issues or resource constraints
**Solutions:**
1. Check Docker Desktop is running
2. Try `make down` then `make up`
3. Check available disk space and memory

### Permission denied errors
**Solutions:**
- Windows: Run terminal as Administrator
- Mac/Linux: Add user to docker group or use `sudo`

## ⚙️ Customizing the Makefile

### Adding New Commands
```makefile
.PHONY: test
test:
	$(PYTHON_CMD) -m pytest tests/

.PHONY: format
format:
	$(PYTHON_CMD) -m black .
	$(PYTHON_CMD) -m isort .
```

### Changing Container Name
```makefile
CONTAINER_NAME = my-python-app
```

### Adding Environment Variables
```makefile
.PHONY: run-dev
run-dev:
	docker exec -it -e DEBUG=1 $(CONTAINER_NAME) python $(FILE)
```

### Multi-stage Commands
```makefile
.PHONY: deploy
deploy: test build
	docker tag $(CONTAINER_NAME) my-registry/$(CONTAINER_NAME):latest
	docker push my-registry/$(CONTAINER_NAME):latest
```

## 🎯 Best Practices

### Use Descriptive Names
```makefile
# Good
.PHONY: run-tests
run-tests:
	$(PYTHON_CMD) -m pytest

# Bad
.PHONY: t
t:
	$(PYTHON_CMD) -m pytest
```

### Add Help Text
```makefile
.PHONY: help
help:
	@echo "Available commands:"
	@echo "  test       - Run test suite"
	@echo "  format     - Format code with black"
```

### Error Handling
```makefile
.PHONY: run
run:
	@if [ -z "$(FILE)" ]; then \
		echo "Error: FILE parameter required"; \
		echo "Usage: make run FILE=script.py"; \
		exit 1; \
	fi
```

### Silent Commands
```makefile
# @ suppresses command echo
.PHONY: quiet-build
quiet-build:
	@docker build -t $(CONTAINER_NAME) . > /dev/null
```

## 📚 Advanced Makefile Features

### Variables from Environment
```makefile
PYTHON_VERSION ?= 3.11
DEBUG ?= 0
```

### Pattern Rules
```makefile
test-%:
	$(PYTHON_CMD) -m pytest tests/test_$*.py
```

### Conditional Targets
```makefile
ifeq ($(OS),Windows_NT)
    SHELL := powershell.exe
endif
```

## 🚀 Next Steps

### Learn More About Make
- [GNU Make Manual](https://www.gnu.org/software/make/manual/)
- [Make Tutorial](https://makefiletutorial.com/)

### Extend Your Makefile
- Add testing commands
- Include code formatting
- Implement deployment scripts
- Create development vs production targets

### Integration Ideas
- CI/CD pipelines
- Git hooks
- IDE integration
- Team development workflows

---

**The Makefile simplifies your development workflow by:**
- 🎯 Providing simple, memorable commands
- 🔄 Automating repetitive tasks
- 📚 Documenting team workflows
- 🛡️ Ensuring consistent environments

**Master these make commands and speed up your Python development!** ⚡