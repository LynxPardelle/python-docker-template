# Library Management Guide

This guide shows you how to add, manage, and use Python libraries in your Docker environment.

## 📦 Quick Library Addition

### 1. Add to requirements.txt
```txt
# Basic libraries (already included)
requests==2.31.0
beautifulsoup4==4.12.2
matplotlib==3.8.0
numpy==1.25.2
pandas==2.1.1

# Add your new libraries here
fastapi==0.104.1
pytest==7.4.3
```

### 2. Rebuild container
```bash
make rebuild
```

### 3. Use in your code
```python
import requests
import fastapi
import pytest
```

## 🔍 Finding Libraries

### Popular Python Libraries by Category

**Web Development:**
- `fastapi` - Modern web API framework
- `flask` - Lightweight web framework
- `django` - Full-featured web framework
- `streamlit` - Data apps and dashboards

**Data Science:**
- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computing
- `matplotlib` - Plotting and visualization
- `seaborn` - Statistical data visualization
- `plotly` - Interactive visualizations
- `scikit-learn` - Machine learning
- `jupyter` - Interactive notebooks

**Web Scraping:**
- `requests` - HTTP requests
- `beautifulsoup4` - HTML/XML parsing
- `scrapy` - Web crawling framework
- `selenium` - Browser automation

**Utilities:**
- `python-dotenv` - Environment variables
- `click` - Command-line interfaces
- `rich` - Rich text and formatting
- `pydantic` - Data validation

**Testing:**
- `pytest` - Testing framework
- `coverage` - Code coverage
- `mock` - Mock objects

### How to Find Libraries

1. **PyPI (Python Package Index)**: https://pypi.org/
2. **Awesome Python**: https://awesome-python.com/
3. **GitHub trending**: https://github.com/trending/python
4. **Search by use case**: "python library for [task]"

## 📋 Requirements.txt Best Practices

### Pin Versions
```txt
# Good - specific versions
requests==2.31.0
pandas==2.1.1

# Avoid - unpinned versions (can break)
requests
pandas
```

### Version Constraints
```txt
# Exact version
requests==2.31.0

# Minimum version
requests>=2.30.0

# Compatible version (safe updates)
requests~=2.31.0

# Version range
requests>=2.30.0,<3.0.0
```

### Group Related Libraries
```txt
# Web development
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.5.0

# Data science
pandas==2.1.1
numpy==1.25.2
matplotlib==3.8.0

# Development tools
pytest==7.4.3
black==23.10.1
flake8==6.1.0
```

### Comments and Documentation
```txt
# Web scraping libraries
requests==2.31.0          # HTTP requests
beautifulsoup4==4.12.2    # HTML parsing

# Data analysis
pandas==2.1.1             # Data manipulation
numpy==1.25.2             # Numerical computing
```

## 🚀 Installation Workflow

### Adding New Libraries

1. **Research the library**:
   ```bash
   # Check PyPI page for latest version and docs
   # Read documentation and examples
   ```

2. **Add to requirements.txt**:
   ```txt
   # Add at the end or in appropriate section
   new-library==1.2.3
   ```

3. **Rebuild container**:
   ```bash
   make rebuild
   ```

4. **Test the installation**:
   ```bash
   make python CMD='-c "import new_library; print(\"Success!\")"'
   ```

5. **Create example usage**:
   ```python
   # In your Python file
   import new_library
   
   # Test basic functionality
   print(new_library.__version__)
   ```

### Removing Libraries

1. **Remove from requirements.txt**:
   ```txt
   # Comment out or delete the line
   # old-library==1.0.0
   ```

2. **Rebuild container**:
   ```bash
   make rebuild
   ```

3. **Verify removal**:
   ```bash
   make python CMD='-c "import old_library"'  # Should fail
   ```

## 🔧 Advanced Library Management

### Development vs Production Dependencies

Create separate requirement files:

**requirements.txt** (production):
```txt
requests==2.31.0
pandas==2.1.1
numpy==1.25.2
```

**requirements-dev.txt** (development):
```txt
-r requirements.txt  # Include production deps
pytest==7.4.3
black==23.10.1
flake8==6.1.0
jupyter==1.0.0
```

Update Dockerfile:
```dockerfile
# Copy both requirement files
COPY requirements*.txt ./

# Install production dependencies
RUN pip install -r requirements.txt

# Conditionally install dev dependencies
ARG INSTALL_DEV=false
RUN if [ "$INSTALL_DEV" = "true" ] ; then pip install -r requirements-dev.txt ; fi
```

### Library Conflicts Resolution

When libraries conflict:

1. **Check compatibility**:
   ```bash
   # Use pip-tools to resolve dependencies
   pip install pip-tools
   pip-compile requirements.in
   ```

2. **Find compatible versions**:
   ```txt
   # Example: library A needs requests>=2.25.0
   # library B needs requests<2.30.0
   # Solution: use requests>=2.25.0,<2.30.0
   ```

3. **Use virtual environments** (in container):
   ```bash
   # Create separate environments for conflicting projects
   python -m venv project1_env
   python -m venv project2_env
   ```

### Security Updates

Regularly update dependencies:

1. **Check for updates**:
   ```bash
   pip list --outdated
   ```

2. **Update safely**:
   ```txt
   # Update to latest compatible version
   requests~=2.31.0  # Will update to 2.31.x but not 2.32.0
   ```

3. **Security scanning**:
   ```bash
   pip install safety
   safety check
   ```

## 📊 Common Library Examples

### Data Analysis Stack
```txt
# requirements.txt for data science
pandas==2.1.1
numpy==1.25.2
matplotlib==3.8.0
seaborn==0.13.0
scipy==1.11.4
statsmodels==0.14.1
```

**Example usage**:
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create sample data
data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})

# Plot
plt.scatter(data['x'], data['y'])
plt.savefig('scatter.png')
```

### Web Scraping Stack
```txt
# requirements.txt for web scraping
requests==2.31.0
beautifulsoup4==4.12.2
lxml==4.9.3
selenium==4.15.2
```

**Example usage**:
```python
import requests
from bs4 import BeautifulSoup

response = requests.get('https://httpbin.org/html')
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.title.text)
```

### API Development Stack
```txt
# requirements.txt for API development
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.5.0
python-dotenv==1.0.0
```

**Example usage**:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Run with: uvicorn main:app --reload
```

## 🐛 Troubleshooting Libraries

### "No module named 'xyz'"

1. **Check if added to requirements.txt**
2. **Rebuild container**: `make rebuild`
3. **Verify installation**: `make python CMD='-c "import xyz"'`

### Import errors after installation

1. **Check for typos**:
   ```python
   import requests  # Correct
   import request   # Wrong
   ```

2. **Check module structure**:
   ```python
   # Some libraries have submodules
   from sklearn.linear_model import LinearRegression
   # Not just: import sklearn
   ```

### Version conflicts

1. **Check dependency tree**:
   ```bash
   pip show library-name
   ```

2. **Use compatible versions**:
   ```txt
   # Find versions that work together
   library-a==1.2.3
   library-b==2.1.0
   ```

### Installation failures

1. **Check system dependencies**:
   ```dockerfile
   # In Dockerfile, add system packages
   RUN apt-get update && apt-get install -y \
       build-essential \
       libpq-dev \
       && rm -rf /var/lib/apt/lists/*
   ```

2. **Use wheel packages**:
   ```bash
   pip install --only-binary=all package-name
   ```

## 🎯 Best Practices Summary

1. **Always pin versions** in requirements.txt
2. **Test after adding libraries** with simple imports
3. **Group related libraries** with comments
4. **Keep requirements.txt clean** - remove unused libraries
5. **Update regularly** but test thoroughly
6. **Use specific versions** for production
7. **Document library purposes** with comments
8. **Separate dev and production** dependencies

## 🚀 Next Steps

### Learn About Specific Libraries
- Read official documentation
- Follow tutorials and examples
- Practice with small projects
- Join community forums

### Advanced Topics
- **Dependency resolution** with pip-tools
- **Virtual environments** within containers
- **Custom package creation** and distribution
- **Private package repositories**

---

**Remember**: The Python ecosystem is vast! Start with popular, well-documented libraries and gradually explore more specialized tools as you build projects.

**Need specific library help?** Check the library's documentation or ask in the Python community!