#!/usr/bin/env python3
"""
Environment Variables Examples

Learn about using environment variables and .env files in Python.

To run: make run FILE=examples/06_environment_variables.py

First, create a .env file: make env-setup
"""

import os
from dotenv import load_dotenv


def main():
    print("🌍 Environment Variables Examples")
    print("=" * 37)
    
    # Load environment variables
    load_env_examples()
    
    # Basic environment variable usage
    basic_env_examples()
    
    # Configuration management
    configuration_examples()
    
    # Security best practices
    security_examples()


def load_env_examples():
    """Examples of loading .env files"""
    print("\n📂 Loading Environment Variables:")
    
    # Load .env file (if it exists)
    env_loaded = load_dotenv()
    
    if env_loaded:
        print("✅ .env file loaded successfully!")
    else:
        print("⚠️  No .env file found")
        print("💡 Run 'make env-setup' to create a .env template")
    
    # You can also load from specific files
    # load_dotenv('.env.development')
    # load_dotenv('.env.production')
    
    print("\n📋 Available environment variables:")
    env_vars = ['PYTHONPATH', 'PYTHON_ENV', 'APP_NAME', 'DEBUG', 'PATH']
    for var in env_vars:
        value = os.getenv(var, 'Not set')
        # Hide sensitive info in PATH
        if var == 'PATH':
            value = f"{value[:50]}..." if len(value) > 50 else value
        print(f"  {var}: {value}")


def basic_env_examples():
    """Examples of basic environment variable operations"""
    print("\n🔧 Basic Environment Variable Operations:")
    
    # Getting environment variables
    app_name = os.getenv('APP_NAME', 'DefaultApp')
    debug_mode = os.getenv('DEBUG', 'false').lower() == 'true'
    python_env = os.getenv('PYTHON_ENV', 'development')
    
    print(f"App Name: {app_name}")
    print(f"Debug Mode: {debug_mode}")
    print(f"Python Environment: {python_env}")
    
    # Setting environment variables (runtime only)
    os.environ['TEMP_VAR'] = 'temporary_value'
    print(f"Temporary Variable: {os.getenv('TEMP_VAR')}")
    
    # Using environment variables with defaults
    database_url = os.getenv('DATABASE_URL', 'sqlite:///default.db')
    api_timeout = int(os.getenv('API_TIMEOUT', '30'))
    max_connections = int(os.getenv('MAX_CONNECTIONS', '10'))
    
    print(f"\n🔗 Configuration with defaults:")
    print(f"Database URL: {database_url}")
    print(f"API Timeout: {api_timeout} seconds")
    print(f"Max Connections: {max_connections}")


def configuration_examples():
    """Examples of using environment variables for configuration"""
    print("\n⚙️ Configuration Management:")
    
    class Config:
        """Configuration class using environment variables"""
        
        def __init__(self):
            # App settings
            self.app_name = os.getenv('APP_NAME', 'PythonApp')
            self.app_version = os.getenv('APP_VERSION', '1.0.0')
            self.debug = os.getenv('DEBUG', 'false').lower() == 'true'
            self.environment = os.getenv('PYTHON_ENV', 'development')
            
            # Database settings (examples)
            self.database_url = os.getenv('DATABASE_URL', 'sqlite:///app.db')
            
            # API settings (examples)
            self.api_key = os.getenv('API_KEY', '')
            self.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key')
            
            # External services (examples)
            self.redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')
            self.email_host = os.getenv('EMAIL_HOST', 'localhost')
            self.email_port = int(os.getenv('EMAIL_PORT', '587'))
        
        def is_development(self):
            return self.environment == 'development'
        
        def is_production(self):
            return self.environment == 'production'
        
        def display_config(self):
            print("Current Configuration:")
            print(f"  📱 App: {self.app_name} v{self.app_version}")
            print(f"  🌍 Environment: {self.environment}")
            print(f"  🐛 Debug Mode: {self.debug}")
            print(f"  🗄️  Database: {self.database_url}")
            print(f"  🔑 API Key: {'Set' if self.api_key else 'Not set'}")
            print(f"  📧 Email Host: {self.email_host}:{self.email_port}")
    
    # Create and use configuration
    config = Config()
    config.display_config()
    
    # Environment-specific behavior
    if config.is_development():
        print("\n🔧 Development mode features enabled:")
        print("  - Detailed error messages")
        print("  - Auto-reload on file changes")
        print("  - Debug logging")
    elif config.is_production():
        print("\n🚀 Production mode features enabled:")
        print("  - Error logging only")
        print("  - Performance optimizations")
        print("  - Security enhancements")


def security_examples():
    """Examples of security best practices with environment variables"""
    print("\n🔒 Security Best Practices:")
    
    # Sensitive data handling
    api_key = os.getenv('API_KEY')
    secret_key = os.getenv('SECRET_KEY')
    
    print("✅ Good practices:")
    print("  - Store secrets in .env file (not in code)")
    print("  - Use strong, unique values for production")
    print("  - Never commit .env files to version control")
    print("  - Use different .env files for different environments")
    
    print("\n🛡️ Security checks:")
    
    # Check if sensitive variables are set
    sensitive_vars = ['SECRET_KEY', 'API_KEY', 'DATABASE_URL']
    for var in sensitive_vars:
        value = os.getenv(var)
        if value:
            # Don't print actual values, just status
            is_default = value in ['dev-secret-key', 'your-secret-key-here', 'sqlite:///app.db']
            if is_default:
                print(f"  ⚠️  {var}: Using default/template value")
            else:
                print(f"  ✅ {var}: Custom value set")
        else:
            print(f"  ❌ {var}: Not set")
    
    # Validation examples
    def validate_environment():
        issues = []
        
        # Check for required variables in production
        if os.getenv('PYTHON_ENV') == 'production':
            required_vars = ['SECRET_KEY', 'DATABASE_URL']
            for var in required_vars:
                if not os.getenv(var):
                    issues.append(f"Missing required variable: {var}")
        
        # Check for weak secrets
        secret = os.getenv('SECRET_KEY', '')
        if secret and len(secret) < 32:
            issues.append("SECRET_KEY should be at least 32 characters long")
        
        return issues
    
    issues = validate_environment()
    if issues:
        print("\n⚠️ Configuration issues found:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("\n✅ Environment configuration looks good!")


def practical_examples():
    """Practical examples of using environment variables"""
    print("\n🎯 Practical Examples:")
    
    # Feature flags
    feature_enabled = os.getenv('FEATURE_NEW_UI', 'false').lower() == 'true'
    if feature_enabled:
        print("🆕 New UI feature is enabled")
    else:
        print("📱 Using classic UI")
    
    # Different behavior based on environment
    env = os.getenv('PYTHON_ENV', 'development')
    
    if env == 'development':
        log_level = 'DEBUG'
        cache_timeout = 0  # No caching in dev
    elif env == 'staging':
        log_level = 'INFO'
        cache_timeout = 300  # 5 minutes
    elif env == 'production':
        log_level = 'WARNING'
        cache_timeout = 3600  # 1 hour
    else:
        log_level = 'INFO'
        cache_timeout = 60  # 1 minute
    
    print(f"\n📊 Environment-specific settings ({env}):")
    print(f"  📝 Log Level: {log_level}")
    print(f"  ⏱️  Cache Timeout: {cache_timeout} seconds")
    
    # URL construction
    host = os.getenv('HOST', 'localhost')
    port = os.getenv('PORT', '8000')
    ssl = os.getenv('USE_SSL', 'false').lower() == 'true'
    
    protocol = 'https' if ssl else 'http'
    base_url = f"{protocol}://{host}:{port}"
    
    print(f"\n🌐 Server configuration:")
    print(f"  Base URL: {base_url}")
    print(f"  SSL Enabled: {ssl}")


if __name__ == "__main__":
    main()
    
    # Bonus: Practical examples
    practical_examples()
    
    print("\n💡 Environment Variable Tips:")
    print("1. Always provide sensible defaults")
    print("2. Validate critical configuration on startup")
    print("3. Use descriptive variable names (ALL_CAPS)")
    print("4. Document your environment variables")
    print("5. Keep secrets out of version control")
    print("\n🔗 Related commands:")
    print("  make env-setup    - Create .env template")
    print("  make env-check    - Validate .env file")
    print("  make env-example  - Create .env.example for sharing")