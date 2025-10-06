#!/usr/bin/env python3
"""
File Handling Examples

Learn about reading from and writing to files in Python.

To run: make run FILE=examples/04_file_handling.py
"""

import os
import json


def main():
    print("📁 File Handling Examples")
    print("=" * 25)
    
    # Create example files
    create_example_files()
    
    # Text file operations
    text_file_examples()
    
    # JSON file operations
    json_file_examples()
    
    # File system operations
    file_system_examples()
    
    # Clean up example files
    cleanup_files()


def create_example_files():
    """Create example files for demonstration"""
    print("\n📝 Creating example files...")
    
    # Create a simple text file
    with open("sample.txt", "w") as file:
        file.write("Hello, Python!\n")
        file.write("This is a sample text file.\n")
        file.write("It contains multiple lines.\n")
        file.write("Perfect for learning file operations!\n")
    
    # Create a CSV-like file
    with open("students.csv", "w") as file:
        file.write("name,age,grade\n")
        file.write("Alice,20,A\n")
        file.write("Bob,19,B\n")
        file.write("Charlie,21,A\n")
        file.write("Diana,20,C\n")
    
    print("✅ Example files created!")


def text_file_examples():
    """Examples of text file operations"""
    print("\n📄 Text File Operations:")
    
    # Reading entire file
    print("Reading entire file:")
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
    
    # Reading line by line
    print("Reading line by line:")
    with open("sample.txt", "r") as file:
        line_number = 1
        for line in file:
            print(f"  Line {line_number}: {line.strip()}")
            line_number += 1
    
    # Reading all lines into a list
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        print(f"Total lines in file: {len(lines)}")
    
    # Writing to a file
    print("\nWriting to a new file:")
    with open("output.txt", "w") as file:
        file.write("This is a new file!\n")
        file.write("Created by Python script.\n")
        
        # Writing a list of items
        items = ["apple", "banana", "cherry"]
        for item in items:
            file.write(f"- {item}\n")
    
    # Appending to a file
    with open("output.txt", "a") as file:
        file.write("\nThis line was appended!\n")
    
    # Reading the created file
    print("Content of the new file:")
    with open("output.txt", "r") as file:
        print(file.read())


def json_file_examples():
    """Examples of JSON file operations"""
    print("\n📊 JSON File Operations:")
    
    # Creating Python data structure
    student_data = {
        "name": "Alice Johnson",
        "age": 22,
        "courses": ["Python", "Math", "Physics"],
        "grades": {
            "Python": "A",
            "Math": "B+",
            "Physics": "A-"
        },
        "is_active": True,
        "graduation_year": None
    }
    
    # Writing JSON to file
    with open("student.json", "w") as file:
        json.dump(student_data, file, indent=2)
    
    print("JSON data written to file!")
    
    # Reading JSON from file
    with open("student.json", "r") as file:
        loaded_data = json.load(file)
    
    print("Loaded JSON data:")
    print(f"Name: {loaded_data['name']}")
    print(f"Age: {loaded_data['age']}")
    print(f"Courses: {', '.join(loaded_data['courses'])}")
    
    # Working with JSON strings
    json_string = json.dumps(student_data, indent=2)
    print("\nJSON as string:")
    print(json_string[:100] + "..." if len(json_string) > 100 else json_string)


def file_system_examples():
    """Examples of file system operations"""
    print("\n🗂️ File System Operations:")
    
    # Check if file exists
    files_to_check = ["sample.txt", "nonexistent.txt", "student.json"]
    for filename in files_to_check:
        if os.path.exists(filename):
            print(f"✅ {filename} exists")
            # Get file size
            size = os.path.getsize(filename)
            print(f"   Size: {size} bytes")
        else:
            print(f"❌ {filename} does not exist")
    
    # List files in current directory
    print(f"\nFiles in current directory:")
    files = os.listdir(".")
    python_files = [f for f in files if f.endswith('.py')]
    other_files = [f for f in files if not f.endswith('.py')]
    
    print("Python files:")
    for file in python_files:
        print(f"  🐍 {file}")
    
    print("Other files:")
    for file in other_files[:10]:  # Limit to first 10
        print(f"  📄 {file}")
    
    # Get current working directory
    current_dir = os.getcwd()
    print(f"\nCurrent directory: {current_dir}")
    
    # File path operations
    file_path = os.path.join("examples", "sample_data.txt")
    print(f"Joined path: {file_path}")
    print(f"Directory name: {os.path.dirname(file_path)}")
    print(f"Base name: {os.path.basename(file_path)}")
    print(f"File extension: {os.path.splitext(file_path)[1]}")


def cleanup_files():
    """Clean up example files"""
    print("\n🧹 Cleaning up example files...")
    
    files_to_remove = ["sample.txt", "students.csv", "output.txt", "student.json"]
    
    for filename in files_to_remove:
        try:
            if os.path.exists(filename):
                os.remove(filename)
                print(f"✅ Removed {filename}")
        except OSError as e:
            print(f"❌ Error removing {filename}: {e}")


# Error handling examples
def error_handling_examples():
    """Examples of error handling with files"""
    print("\n⚠️ Error Handling Examples:")
    
    # Try to read a non-existent file
    try:
        with open("nonexistent.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("❌ File not found - handled gracefully!")
    except PermissionError:
        print("❌ Permission denied - handled gracefully!")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    else:
        print("✅ File read successfully!")
    finally:
        print("🔄 This always executes (cleanup code goes here)")


if __name__ == "__main__":
    main()
    
    # Bonus: Error handling
    error_handling_examples()
    
    print("\n🎯 File Handling Tips:")
    print("1. Always use 'with' statement for file operations")
    print("2. Handle exceptions when working with files")
    print("3. Use appropriate file modes: 'r' (read), 'w' (write), 'a' (append)")
    print("4. Use JSON for structured data storage")
    print("5. Check if files exist before operating on them")