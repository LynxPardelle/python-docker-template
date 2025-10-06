#!/usr/bin/env python3
"""
Welcome to Python Learning with Docker!

This is the main entry point for your Python learning journey.
You can modify this file to practice different Python concepts.

To run this file:
1. Make sure your container is running: make up
2. Run this file: make run FILE=main.py

New features:
- Environment variables support (create .env with: make env-setup)
- Automatic library management (add packages with: make add PKG=package-name)
"""

import os
try:
    from dotenv import load_dotenv
    load_dotenv()  # Load environment variables from .env file
except ImportError:
    # dotenv not installed yet, that's okay
    pass

def main():
    """
    Main function - This is where your code starts running.
    Practice different Python concepts by modifying the code below.
    """
    print("🐍 Welcome to Python Learning with Docker! 🐳")
    print("=" * 50)
    
    # Show environment configuration
    show_environment_info()
    
    # Practice basic Python concepts here
    practice_variables()
    practice_basic_operations()
    practice_data_types()
    
    print("\n" + "=" * 50)
    print("✅ Great job! You've completed the basic examples.")
    print("📚 Check the 'examples/' folder for more learning materials.")
    print("📖 Visit 'docs/' folder for detailed documentation.")
    print("\n🆕 New Features:")
    print("  🌍 Environment variables: make env-setup")
    print("  📦 Auto library install: make add PKG=requests")
    print("  📝 See all commands: make help")


def practice_variables():
    """Practice working with variables"""
    print("\n📝 Variables Practice:")
    
    # Different types of variables
    name = "Python Learner"
    age = 25
    height = 5.9
    is_learning = True
    
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height} feet")
    print(f"Currently learning: {is_learning}")


def practice_basic_operations():
    """Practice basic mathematical operations"""
    print("\n🧮 Basic Operations Practice:")
    
    a = 10
    b = 3
    
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b:.2f}")
    print(f"{a} ** {b} = {a ** b}")


def show_environment_info():
    """Show environment configuration and available features"""
    print("\n🌍 Environment Information:")
    
    # Get environment variables with defaults
    app_name = os.getenv('APP_NAME', 'PythonDockerApp')
    python_env = os.getenv('PYTHON_ENV', 'development')
    debug = os.getenv('DEBUG', 'false').lower() == 'true'
    
    print(f"  📱 App Name: {app_name}")
    print(f"  🌍 Environment: {python_env}")
    print(f"  🐛 Debug Mode: {debug}")
    
    # Check if .env file exists
    if os.path.exists('.env'):
        print("  ✅ .env file found")
    else:
        print("  ⚠️  No .env file (create with: make env-setup)")


def practice_data_types():
    """Practice different data types"""
    print("\n📊 Data Types Practice:")
    
    # List
    fruits = ["apple", "banana", "orange"]
    print(f"Fruits list: {fruits}")
    
    # Dictionary
    person = {"name": "Alice", "age": 30, "city": "New York"}
    print(f"Person info: {person}")
    
    # Tuple
    coordinates = (10, 20)
    print(f"Coordinates: {coordinates}")
    
    # Set
    unique_numbers = {1, 2, 3, 3, 4, 4, 5}
    print(f"Unique numbers: {unique_numbers}")


if __name__ == "__main__":
    # This ensures the main() function only runs when this file is executed directly
    main()