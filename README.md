# Python Docker Template 🐍🐳

A complete, beginner-friendly Python development environment using Docker. Perfect for learning Python without the hassle of local setup!

## ✨ Features

- **🐍 Python 3.11** - Latest stable Python version
- **🐳 Docker & Docker Compose** - Consistent environment across all systems
- **📁 Volume Mounting** - Instant file sync between host and container
- **📦 Package Management** - Easy library installation via requirements.txt
- **🔧 Makefile Automation** - Simple commands for common tasks
- **📚 Learning Examples** - Step-by-step Python tutorials
- **📖 Comprehensive Docs** - Detailed guides for beginners
- **🛡️ Security** - Non-root user for safe execution

## 🚀 Quick Start (5 Minutes)

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed
- **Windows**: [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install) (recommended) or [Make](https://chocolatey.org/packages/make)
- **Mac/Linux**: Make (usually pre-installed)

### Get Started
```bash
# 1. Clone or download this repository
git clone <your-repo-url>
cd python-docker-template

# 2. Build and start the environment
make up

# 3. Run your first Python program
make run FILE=main.py

# 4. Try the learning examples
make run FILE=examples/01_variables.py
```

**That's it!** You now have a complete Python development environment running in Docker.

## 📋 Essential Commands

```bash
# Environment Management
make up          # Start the Docker container
make down        # Stop and remove the container
make rebuild     # Rebuild after adding new libraries
make status      # Check container status

# Running Python Code
make run FILE=filename.py           # Run a specific Python file
make python CMD='-c "print(42)"'    # Run Python commands directly
make shell                          # Open interactive shell in container

# Library Management
make add PKG=requests               # Add and install new package
make remove PKG=requests            # Remove package from requirements
make list-packages                  # Show all installed packages
make update-deps                    # Update all packages to latest versions

# Environment Variables
make env-setup                      # Create .env template file
make env-check                      # Validate .env file format

# Development
make install     # Rebuild container with new requirements
make logs        # View container logs
make clean       # Remove all containers and images
make help        # Show all available commands
```

## 📁 Project Structure

```
python-docker-template/
├── 📄 main.py              # Your main Python file - start here!
├── 📁 examples/            # Learning examples (run these in order)
│   ├── 01_variables.py     # Variables and data types
│   ├── 02_control_flow.py  # If statements and loops
│   ├── 03_functions.py     # Functions and modules
│   ├── 04_file_handling.py # Working with files
│   ├── 05_libraries.py     # Using external libraries
│   └── 06_environment_variables.py # Environment variables and .env files
├── 📁 docs/                # Comprehensive documentation
│   ├── getting-started.md  # Step-by-step setup guide
│   ├── python-guide.md     # Complete Python tutorial
│   ├── docker-guide.md     # Docker concepts explained
│   └── ...more guides...   # Additional documentation
├── 📄 requirements.txt     # Python packages (add new ones here)
├── 📄 Dockerfile          # Container configuration
├── 📄 docker-compose.yml  # Container orchestration
├── 📄 Makefile            # Automation commands
└── 📄 README.md           # This file
```

## 🎓 Learning Path

### For Complete Beginners
1. **Start Here**: Read [Getting Started Guide](docs/getting-started.md)
2. **Learn Python**: Follow [Python Guide](docs/python-guide.md)
3. **Practice**: Run examples in order:
   ```bash
   make run FILE=examples/01_variables.py
   make run FILE=examples/02_control_flow.py
   make run FILE=examples/03_functions.py
   make run FILE=examples/04_file_handling.py
   make run FILE=examples/05_libraries.py
   make run FILE=examples/06_environment_variables.py
   ```

### For Docker Beginners
1. **Understand Containers**: [Docker Guide](docs/docker-guide.md)
2. **Multi-container Setup**: [Docker Compose Guide](docs/docker-compose-guide.md)
3. **Automation**: [Makefile Guide](docs/makefile-guide.md)

### For Developers
1. **Daily Workflow**: [Development Workflow](docs/development-workflow.md)
2. **Adding Libraries**: [Library Management](docs/library-management.md)
3. **Best Practices**: [Security & Performance](docs/best-practices.md)

## 📦 Adding New Libraries

### Automatic Method (Recommended)
```bash
# Add package automatically
make add PKG=requests
make add PKG='fastapi==0.104.1'

# Rebuild container
make rebuild
```

### Manual Method
1. **Add to requirements.txt**:
   ```txt
   numpy==1.25.2
   pandas==2.1.1
   requests==2.31.0
   ```

2. **Rebuild container**:
   ```bash
   make rebuild
   ```

3. **Use in your code**:
   ```python
   import numpy as np
   import pandas as pd
   import requests
   ```

## 🌍 Environment Variables

```bash
# Create .env template
make env-setup

# Edit .env file with your values
# Then use in Python:
```

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')
app_name = os.getenv('APP_NAME', 'DefaultApp')
```

## 💡 Usage Examples

### Basic Python Script
```python
#!/usr/bin/env python3
# save as: my_script.py

def main():
    print("Hello from Docker!")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")

if __name__ == "__main__":
    main()
```

Run with: `make run FILE=my_script.py`

### Web Scraping Example
```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://httpbin.org/json")
data = response.json()
print(f"Origin IP: {data['origin']}")
```

### Data Analysis Example
```python
import pandas as pd
import numpy as np

# Create sample data
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [70000, 80000, 90000]
}

df = pd.DataFrame(data)
print(df.describe())
```

## 🔧 Customization

### Change Python Version
Edit `Dockerfile`:
```dockerfile
FROM python:3.12-slim  # Change version here
```

### Add System Dependencies
Edit `Dockerfile`:
```dockerfile
RUN apt-get update && apt-get install -y \
    gcc \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*
```

### Modify Container Settings
Edit `docker-compose.yml`:
```yaml
services:
  python-app:
    ports:
      - "8000:8000"  # Expose ports
    environment:
      - DEBUG=1       # Add environment variables
```

## 🛠️ Troubleshooting

### Common Issues

**Container won't start?**
```bash
make clean    # Remove everything
make up       # Start fresh
```

**Permission denied?**
- Windows: Run terminal as Administrator
- Mac/Linux: `sudo make up`

**File changes not reflected?**
```bash
make rebuild  # Rebuild container
```

**Import errors?**
1. Add library to `requirements.txt`
2. Run `make rebuild`

### Get Help
- 📖 Check [Troubleshooting Guide](docs/troubleshooting.md)
- 📚 Read specific component guides in `docs/`
- 🔍 Review examples in `examples/`

## 🎯 What You Can Build

With this template, you can create:

- **🤖 Automation Scripts** - File processing, system tasks
- **🌐 Web Scrapers** - Data collection from websites
- **📊 Data Analysis** - CSV processing, statistics, visualization
- **🔌 API Clients** - Interact with REST APIs
- **🎮 Simple Games** - Console-based games and puzzles
- **📱 CLI Tools** - Command-line utilities
- **📈 Reports** - Automated report generation

## 🤝 Contributing

Found a bug or want to add a feature?

1. Fork this repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments

- **Python Software Foundation** - For the amazing Python language
- **Docker Inc.** - For containerization technology
- **Community Contributors** - For examples and improvements

---

**Ready to start coding?** 🚀

```bash
make up
make run FILE=main.py
```

**Happy coding!** 🐍🐳