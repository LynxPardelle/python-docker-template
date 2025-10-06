# Variables
CONTAINER_NAME = python-learning
PYTHON_CMD = docker exec -it $(CONTAINER_NAME) python
PIP_CMD = docker exec -it $(CONTAINER_NAME) pip
REQ_FILE = requirements.txt
REQ_DEV_FILE = requirements-dev.txt

# Help command - shows all available commands
.PHONY: help
help:
	@echo "Available commands:"
	@echo "  build          - Build the Docker image"
	@echo "  up             - Start the container in detached mode"
	@echo "  down           - Stop and remove the container"
	@echo "  rebuild        - Stop, rebuild and start the container"
	@echo "  shell          - Open interactive shell in the container"
	@echo "  run FILE=<file> - Run a specific Python file (e.g., make run FILE=main.py)"
	@echo "  python CMD=<cmd> - Run any Python command (e.g., make python CMD='-c \"print(2+2)\"')"
	@echo "  install        - Rebuild container after adding new requirements"
	@echo "  logs           - Show container logs"
	@echo "  clean          - Remove all containers and images"
	@echo "  status         - Show container status"
	@echo ""
	@echo "Library Management:"
	@echo "  add PKG=<package> - Add and install a new package (e.g., make add PKG=requests)"
	@echo "  add-dev PKG=<package> - Add package to dev requirements"
	@echo "  remove PKG=<package> - Remove package from requirements"
	@echo "  update-deps    - Update all packages to latest versions"
	@echo "  freeze         - Update requirements.txt with currently installed packages"
	@echo "  list-packages  - Show all installed packages"
	@echo ""
	@echo "Environment Management:"
	@echo "  env-setup      - Create .env template file"
	@echo "  env-check      - Validate .env file format"
	@echo "  env-example    - Create .env.example from .env"

# Build the Docker image
.PHONY: build
build:
	docker-compose build

# Start the container
.PHONY: up
up:
	docker-compose up -d

# Stop and remove the container
.PHONY: down
down:
	docker-compose down

# Rebuild and restart (useful after changing requirements.txt)
.PHONY: rebuild
rebuild: down build up
	@echo "Container rebuilt and restarted!"

# Open interactive shell in the container
.PHONY: shell
shell:
	docker exec -it $(CONTAINER_NAME) /bin/bash

# Run a specific Python file
.PHONY: run
run:
	@if [ -z "$(FILE)" ]; then \
		echo "Usage: make run FILE=<filename>"; \
		echo "Example: make run FILE=main.py"; \
	else \
		$(PYTHON_CMD) $(FILE); \
	fi

# Run any Python command
.PHONY: python
python:
	@if [ -z "$(CMD)" ]; then \
		echo "Usage: make python CMD='<command>'"; \
		echo "Example: make python CMD='-c \"print(2+2)\"'"; \
		echo "Example: make python CMD='--version'"; \
	else \
		$(PYTHON_CMD) $(CMD); \
	fi

# Install new requirements (rebuild container)
.PHONY: install
install: rebuild
	@echo "Requirements installed and container rebuilt!"

# Show container logs
.PHONY: logs
logs:
	docker logs $(CONTAINER_NAME)

# Clean up everything
.PHONY: clean
clean:
	docker-compose down --rmi all --volumes
	docker system prune -f

# Show container status
.PHONY: status
status:
	docker ps -f name=$(CONTAINER_NAME)

# Library Management Commands

# Add a new package and update requirements.txt
.PHONY: add
add:
	@if [ -z "$(PKG)" ]; then \
		echo "Usage: make add PKG=<package-name>"; \
		echo "Example: make add PKG=requests"; \
		echo "Example: make add PKG='fastapi==0.104.1'"; \
	else \
		echo "Installing $(PKG)..."; \
		$(PIP_CMD) install $(PKG); \
		echo "Updating requirements.txt..."; \
		$(PIP_CMD) freeze > $(REQ_FILE).tmp; \
		grep -E "^(requests|beautifulsoup4|matplotlib|numpy|pandas|$(shell echo $(PKG) | cut -d'=' -f1))" $(REQ_FILE).tmp > $(REQ_FILE).new || true; \
		if [ -s $(REQ_FILE).new ]; then \
			echo "# Basic Python libraries for beginners" > $(REQ_FILE); \
			echo "# Add any new libraries here and rebuild the container" >> $(REQ_FILE); \
			echo "" >> $(REQ_FILE); \
			echo "# Popular external libraries for learning" >> $(REQ_FILE); \
			cat $(REQ_FILE).new >> $(REQ_FILE); \
		else \
			echo "$(PKG)" >> $(REQ_FILE); \
		fi; \
		rm -f $(REQ_FILE).tmp $(REQ_FILE).new; \
		echo "✅ $(PKG) added to requirements.txt"; \
		echo "📦 Run 'make rebuild' to apply changes to container"; \
	fi

# Add a package to development requirements
.PHONY: add-dev
add-dev:
	@if [ -z "$(PKG)" ]; then \
		echo "Usage: make add-dev PKG=<package-name>"; \
		echo "Example: make add-dev PKG=pytest"; \
	else \
		if [ ! -f $(REQ_DEV_FILE) ]; then \
			echo "# Development dependencies" > $(REQ_DEV_FILE); \
			echo "-r requirements.txt" >> $(REQ_DEV_FILE); \
			echo "" >> $(REQ_DEV_FILE); \
		fi; \
		echo "Installing $(PKG)..."; \
		$(PIP_CMD) install $(PKG); \
		echo "$(PKG)" >> $(REQ_DEV_FILE); \
		echo "✅ $(PKG) added to requirements-dev.txt"; \
	fi

# Remove a package from requirements
.PHONY: remove
remove:
	@if [ -z "$(PKG)" ]; then \
		echo "Usage: make remove PKG=<package-name>"; \
		echo "Example: make remove PKG=requests"; \
	else \
		echo "Removing $(PKG)..."; \
		$(PIP_CMD) uninstall -y $(PKG) || true; \
		grep -v "^$(PKG)" $(REQ_FILE) > $(REQ_FILE).tmp || true; \
		mv $(REQ_FILE).tmp $(REQ_FILE); \
		if [ -f $(REQ_DEV_FILE) ]; then \
			grep -v "^$(PKG)" $(REQ_DEV_FILE) > $(REQ_DEV_FILE).tmp || true; \
			mv $(REQ_DEV_FILE).tmp $(REQ_DEV_FILE); \
		fi; \
		echo "✅ $(PKG) removed from requirements"; \
	fi

# Update all packages to latest versions
.PHONY: update-deps
update-deps:
	@echo "Updating all packages to latest versions..."
	$(PIP_CMD) list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 $(PIP_CMD) install -U
	@echo "Updating requirements.txt..."
	make freeze
	@echo "✅ All packages updated"
	@echo "📦 Run 'make rebuild' to apply changes to container"

# Freeze current packages to requirements.txt
.PHONY: freeze
freeze:
	@echo "Freezing current packages to requirements.txt..."
	$(PIP_CMD) freeze > $(REQ_FILE).tmp
	echo "# Basic Python libraries for beginners" > $(REQ_FILE)
	echo "# Add any new libraries here and rebuild the container" >> $(REQ_FILE)
	echo "" >> $(REQ_FILE)
	echo "# Popular external libraries for learning" >> $(REQ_FILE)
	cat $(REQ_FILE).tmp >> $(REQ_FILE)
	rm $(REQ_FILE).tmp
	@echo "✅ requirements.txt updated with current packages"

# List all installed packages
.PHONY: list-packages
list-packages:
	@echo "📦 Installed packages:"
	$(PIP_CMD) list

# Environment Management Commands

# Create .env template file
.PHONY: env-setup
env-setup:
	@if [ -f .env ]; then \
		echo "⚠️  .env file already exists"; \
		echo "📄 Use 'make env-check' to validate it"; \
	else \
		echo "Creating .env template..."; \
		echo "# Environment Variables for Python Docker Template" > .env; \
		echo "# Copy this file and rename to .env, then fill in your values" >> .env; \
		echo "" >> .env; \
		echo "# Python Environment" >> .env; \
		echo "PYTHONPATH=/app" >> .env; \
		echo "PYTHON_ENV=development" >> .env; \
		echo "" >> .env; \
		echo "# Application Settings" >> .env; \
		echo "APP_NAME=PythonDockerApp" >> .env; \
		echo "APP_VERSION=1.0.0" >> .env; \
		echo "DEBUG=true" >> .env; \
		echo "" >> .env; \
		echo "# Database (example)" >> .env; \
		echo "# DATABASE_URL=sqlite:///./app.db" >> .env; \
		echo "" >> .env; \
		echo "# API Keys (example)" >> .env; \
		echo "# API_KEY=your-secret-api-key-here" >> .env; \
		echo "# SECRET_KEY=your-secret-key-here" >> .env; \
		echo "" >> .env; \
		echo "# External Services (example)" >> .env; \
		echo "# REDIS_URL=redis://localhost:6379" >> .env; \
		echo "# EMAIL_HOST=smtp.gmail.com" >> .env; \
		echo "# EMAIL_PORT=587" >> .env; \
		echo "✅ .env template created"; \
		echo "📝 Edit .env file with your actual values"; \
		echo "🔒 Remember: .env is in .gitignore for security"; \
	fi

# Validate .env file format
.PHONY: env-check
env-check:
	@if [ ! -f .env ]; then \
		echo "❌ .env file not found"; \
		echo "📄 Run 'make env-setup' to create one"; \
	else \
		echo "🔍 Checking .env file..."; \
		if grep -q "^[A-Z_][A-Z0-9_]*=" .env; then \
			echo "✅ .env file format looks good"; \
			echo "📊 Variables found:"; \
			grep "^[A-Z_]" .env | cut -d'=' -f1 | sed 's/^/  - /'; \
		else \
			echo "⚠️  No valid environment variables found"; \
			echo "💡 Variables should be in format: VARIABLE_NAME=value"; \
		fi; \
	fi

# Create .env.example from .env
.PHONY: env-example
env-example:
	@if [ ! -f .env ]; then \
		echo "❌ .env file not found"; \
		echo "📄 Run 'make env-setup' first"; \
	else \
		echo "Creating .env.example from .env..."; \
		sed 's/=.*/=/' .env > .env.example; \
		echo "✅ .env.example created"; \
		echo "📤 Safe to commit .env.example to version control"; \
	fi