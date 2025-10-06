# Environment Variables Guide

This guide covers managing environment variables and .env files in your Python Docker template for secure configuration management.

## 🌍 What are Environment Variables?

Environment variables are key-value pairs that exist outside your code and can affect how your program behaves. They're essential for:

- **Configuration** - Settings that change between environments
- **Security** - Storing sensitive data like API keys and passwords
- **Flexibility** - Changing behavior without modifying code
- **Deployment** - Different settings for development, staging, and production

## 🚀 Quick Start

### 1. Create .env file
```bash
make env-setup
```

### 2. Edit your .env file
```bash
# Open .env in your editor and fill in actual values
```

### 3. Use in your Python code
```python
from dotenv import load_dotenv
import os

load_dotenv()
app_name = os.getenv('APP_NAME', 'DefaultApp')
```

### 4. Test environment variables
```bash
make run FILE=examples/06_environment_variables.py
```

## 📁 File Structure for Environment Management

```
python-docker-template/
├── .env                 # Your actual environment variables (never commit!)
├── .env.example         # Template for sharing (safe to commit)
├── .env.development     # Development-specific settings
├── .env.production      # Production-specific settings
└── examples/
    └── 06_environment_variables.py  # Usage examples
```

## 🔧 Make Commands for Environment Management

### Environment Setup
```bash
# Create .env template file
make env-setup

# Validate .env file format
make env-check

# Create .env.example from .env (for sharing)
make env-example
```

### Library Management
```bash
# Add a new package
make add PKG=requests
make add PKG='fastapi==0.104.1'

# Add development packages
make add-dev PKG=pytest
make add-dev PKG=black

# Remove packages
make remove PKG=requests

# Update all packages
make update-deps

# Show installed packages
make list-packages

# Update requirements.txt with current packages
make freeze
```

## 🔐 .env File Structure

When you run `make env-setup`, it creates a template like this:

```env
# Environment Variables for Python Docker Template
# Copy this file and rename to .env, then fill in your values

# Python Environment
PYTHONPATH=/app
PYTHON_ENV=development

# Application Settings
APP_NAME=PythonDockerApp
APP_VERSION=1.0.0
DEBUG=true

# Database (example)
# DATABASE_URL=sqlite:///./app.db

# API Keys (example)
# API_KEY=your-secret-api-key-here
# SECRET_KEY=your-secret-key-here

# External Services (example)
# REDIS_URL=redis://localhost:6379
# EMAIL_HOST=smtp.gmail.com
# EMAIL_PORT=587
```

## 🐍 Using Environment Variables in Python

### Basic Usage
```python
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get environment variables with defaults
app_name = os.getenv('APP_NAME', 'DefaultApp')
debug = os.getenv('DEBUG', 'false').lower() == 'true'
port = int(os.getenv('PORT', '8000'))

print(f"Running {app_name} on port {port}")
if debug:
    print("Debug mode enabled")
```

### Configuration Class Pattern
```python
import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        
        # App settings
        self.app_name = os.getenv('APP_NAME', 'MyApp')
        self.debug = os.getenv('DEBUG', 'false').lower() == 'true'
        self.environment = os.getenv('PYTHON_ENV', 'development')
        
        # Database
        self.database_url = os.getenv('DATABASE_URL', 'sqlite:///app.db')
        
        # Security
        self.secret_key = os.getenv('SECRET_KEY', self._generate_secret_key())
        
        # API settings
        self.api_key = os.getenv('API_KEY')
        self.api_timeout = int(os.getenv('API_TIMEOUT', '30'))
    
    def _generate_secret_key(self):
        if self.environment == 'production':
            raise ValueError("SECRET_KEY must be set in production")
        return 'dev-secret-key-not-for-production'
    
    def is_development(self):
        return self.environment == 'development'

# Usage
config = Config()
```

### Environment-Specific Behavior
```python
import os

env = os.getenv('PYTHON_ENV', 'development')

if env == 'development':
    # Development settings
    DEBUG = True
    DATABASE_URL = 'sqlite:///dev.db'
    LOG_LEVEL = 'DEBUG'
elif env == 'production':
    # Production settings  
    DEBUG = False
    DATABASE_URL = os.getenv('DATABASE_URL')  # Must be set
    LOG_LEVEL = 'WARNING'
else:
    # Default/staging settings
    DEBUG = False
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    LOG_LEVEL = 'INFO'
```

## 📦 Library Management Workflow

### Adding New Libraries

**Method 1: Using make commands (Recommended)**
```bash
# Add a package and update requirements.txt automatically
make add PKG=requests

# Add with specific version
make add PKG='fastapi==0.104.1'

# Add development-only package
make add-dev PKG=pytest
```

**Method 2: Manual method**
```bash
# 1. Add to requirements.txt
echo "requests==2.31.0" >> requirements.txt

# 2. Rebuild container
make rebuild
```

### Removing Libraries
```bash
# Remove package and update requirements
make remove PKG=requests

# Then rebuild container
make rebuild
```

### Updating Libraries
```bash
# Update all packages to latest versions
make update-deps

# Or update requirements.txt with currently installed packages
make freeze

# Rebuild container with updates
make rebuild
```

### Managing Development Dependencies

Create separate requirements files:

**requirements.txt** (production):
```txt
requests==2.31.0
fastapi==0.104.1
```

**requirements-dev.txt** (development):
```txt
-r requirements.txt
pytest==7.4.3
black==23.10.1
flake8==6.1.0
```

Add dev packages:
```bash
make add-dev PKG=pytest
make add-dev PKG=black
```

## 🔒 Security Best Practices

### What to Put in .env
```env
# ✅ Good for .env
SECRET_KEY=your-actual-secret-key-here
DATABASE_PASSWORD=your-db-password
API_KEY=your-api-key
STRIPE_SECRET_KEY=sk_live_...

# ❌ Don't put in .env (use code defaults instead)
APP_NAME=MyApp
DEBUG=false
LOG_LEVEL=INFO
```

### Security Checklist
1. **Never commit .env files** - They're in .gitignore
2. **Use strong secrets** - At least 32 characters for SECRET_KEY
3. **Different values per environment** - Dev, staging, production
4. **Validate required variables** - Fail fast if missing
5. **Use .env.example** - Template for team members

### Validation Example
```python
import os
import sys

def validate_environment():
    """Validate required environment variables"""
    required_vars = {
        'SECRET_KEY': 'Must be at least 32 characters',
        'DATABASE_URL': 'Database connection string required'
    }
    
    missing = []
    invalid = []
    
    for var, description in required_vars.items():
        value = os.getenv(var)
        if not value:
            missing.append(f"{var}: {description}")
        elif var == 'SECRET_KEY' and len(value) < 32:
            invalid.append(f"{var}: Must be at least 32 characters")
    
    if missing or invalid:
        print("❌ Environment validation failed:")
        for item in missing + invalid:
            print(f"  - {item}")
        sys.exit(1)
    
    print("✅ Environment validation passed")

# Call this at app startup
validate_environment()
```

## 🌐 Docker Integration

### Docker Compose Configuration

The template automatically loads .env files:

```yaml
services:
  python-app:
    build: .
    container_name: python-learning
    env_file:
      - .env  # Automatically loaded
    environment:
      - PYTHONUNBUFFERED=1  # Override or add more
```

### Environment Variable Precedence

1. **Command line** - `docker run -e VAR=value`
2. **docker-compose environment** - In docker-compose.yml
3. **.env file** - Your .env file
4. **Dockerfile ENV** - Default values in Dockerfile
5. **Python defaults** - `os.getenv('VAR', 'default')`

### Container Environment Variables
```bash
# Check environment inside container
make shell
printenv | grep -E "(PYTHON|APP|DEBUG)"

# Or from Python
make python CMD='-c "import os; print(dict(os.environ))"'
```

## 🔄 Different Environment Setups

### Development Environment
```env
# .env (development)
PYTHON_ENV=development
DEBUG=true
DATABASE_URL=sqlite:///dev.db
LOG_LEVEL=DEBUG
SECRET_KEY=dev-secret-key-change-in-production
```

### Production Environment
```env
# .env (production)
PYTHON_ENV=production
DEBUG=false
DATABASE_URL=postgresql://user:pass@host:5432/db
LOG_LEVEL=WARNING
SECRET_KEY=super-secure-production-key-32chars
API_KEY=prod-api-key-here
```

### Staging Environment
```env
# .env (staging)
PYTHON_ENV=staging
DEBUG=false
DATABASE_URL=postgresql://user:pass@staging-host:5432/db
LOG_LEVEL=INFO
SECRET_KEY=staging-secret-key-different-from-prod
API_KEY=staging-api-key-here
```

## 🛠️ Troubleshooting

### Common Issues

**"Environment variable not found"**
```bash
# Check if .env file exists
ls -la .env

# Validate .env file
make env-check

# Check if variable is loaded
make python CMD='-c "import os; print(os.getenv(\"VARIABLE_NAME\"))"'
```

**"dotenv module not found"**
```bash
# Install python-dotenv
make add PKG=python-dotenv
make rebuild
```

**"Variables not loading in container"**
```bash
# Restart container after .env changes
make down
make up

# Check docker-compose.yml has env_file section
```

### Debugging Environment Variables
```python
import os

# Print all environment variables
for key, value in os.environ.items():
    if 'SECRET' not in key.upper():  # Don't print secrets
        print(f"{key}={value}")

# Check if .env file is being loaded
from dotenv import load_dotenv
result = load_dotenv()
print(f".env loaded: {result}")

# Check specific variable
var_value = os.getenv('APP_NAME')
print(f"APP_NAME: {var_value or 'Not set'}")
```

## 📚 Real-World Examples

### Web API Configuration
```python
import os
from dotenv import load_dotenv

load_dotenv()

class APIConfig:
    # Server settings
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', '8000'))
    
    # Database
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///api.db')
    
    # Security
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256')
    
    # External APIs
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
    
    # Features
    ENABLE_CORS = os.getenv('ENABLE_CORS', 'false').lower() == 'true'
    RATE_LIMIT = int(os.getenv('RATE_LIMIT', '100'))
```

### Data Science Project
```python
import os
from dotenv import load_dotenv

load_dotenv()

class DataConfig:
    # Data sources
    DATA_DIR = os.getenv('DATA_DIR', './data')
    CSV_PATH = os.getenv('CSV_PATH', './data/dataset.csv')
    
    # Model settings
    MODEL_PATH = os.getenv('MODEL_PATH', './models')
    RANDOM_SEED = int(os.getenv('RANDOM_SEED', '42'))
    
    # Processing
    BATCH_SIZE = int(os.getenv('BATCH_SIZE', '32'))
    MAX_WORKERS = int(os.getenv('MAX_WORKERS', '4'))
    
    # Output
    OUTPUT_DIR = os.getenv('OUTPUT_DIR', './output')
    SAVE_PLOTS = os.getenv('SAVE_PLOTS', 'true').lower() == 'true'
```

## 🎯 Best Practices Summary

### Environment Variables
1. **Use descriptive names** - `DATABASE_URL` not `DB`
2. **ALL_CAPS convention** - Standard naming
3. **Provide defaults** - `os.getenv('VAR', 'default')`
4. **Validate early** - Check required vars at startup
5. **Document variables** - Use .env.example

### Security
1. **Never commit .env** - Use .gitignore
2. **Use different secrets** - Per environment
3. **Strong secret keys** - At least 32 characters
4. **Least privilege** - Only necessary permissions
5. **Rotate secrets** - Regularly update keys

### Development Workflow
1. **Use make commands** - Automated library management
2. **Separate dev/prod deps** - requirements-dev.txt
3. **Version pinning** - Specific package versions
4. **Regular updates** - Keep dependencies current
5. **Container rebuilds** - After dependency changes

---

**Environment variables make your Python applications configurable, secure, and deployable across different environments!** 🌍🔐

**Next steps:**
- Create your .env file: `make env-setup`
- Try the examples: `make run FILE=examples/06_environment_variables.py`
- Add some packages: `make add PKG=requests`