#!/usr/bin/env python3
"""
Variables and Data Types Examples

Learn about different types of variables and data structures in Python.

To run: make run FILE=examples/01_variables.py
"""

def main():
    print("🔢 Variables and Data Types Examples")
    print("=" * 40)
    
    # Basic data types
    basic_types_example()
    
    # String operations
    string_operations_example()
    
    # Lists and operations
    list_operations_example()
    
    # Dictionaries
    dictionary_operations_example()


def basic_types_example():
    """Examples of basic Python data types"""
    print("\n📋 Basic Data Types:")
    
    # Numbers
    integer_number = 42
    float_number = 3.14159
    
    # Strings
    single_quoted = 'Hello'
    double_quoted = "World"
    
    # Booleans
    is_true = True
    is_false = False
    
    # None type
    empty_value = None
    
    print(f"Integer: {integer_number} (type: {type(integer_number).__name__})")
    print(f"Float: {float_number} (type: {type(float_number).__name__})")
    print(f"String: {single_quoted} {double_quoted} (type: {type(single_quoted).__name__})")
    print(f"Boolean: {is_true}, {is_false} (type: {type(is_true).__name__})")
    print(f"None: {empty_value} (type: {type(empty_value).__name__})")


def string_operations_example():
    """Examples of string operations"""
    print("\n📝 String Operations:")
    
    name = "Python"
    version = "3.11"
    
    # String concatenation
    message = name + " " + version
    print(f"Concatenation: {message}")
    
    # String formatting
    formatted = f"Welcome to {name} version {version}!"
    print(f"F-string: {formatted}")
    
    # String methods
    text = "  Hello World  "
    print(f"Original: '{text}'")
    print(f"Upper: '{text.upper()}'")
    print(f"Lower: '{text.lower()}'")
    print(f"Stripped: '{text.strip()}'")
    print(f"Length: {len(text)}")


def list_operations_example():
    """Examples of list operations"""
    print("\n📚 List Operations:")
    
    # Creating lists
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]
    
    print(f"Numbers: {numbers}")
    print(f"Mixed types: {mixed}")
    
    # List operations
    numbers.append(6)  # Add element
    print(f"After append: {numbers}")
    
    numbers.insert(0, 0)  # Insert at position
    print(f"After insert: {numbers}")
    
    removed = numbers.pop()  # Remove last element
    print(f"Removed {removed}, remaining: {numbers}")
    
    # List slicing
    print(f"First 3 elements: {numbers[:3]}")
    print(f"Last 3 elements: {numbers[-3:]}")


def dictionary_operations_example():
    """Examples of dictionary operations"""
    print("\n📖 Dictionary Operations:")
    
    # Creating dictionaries
    student = {
        "name": "Alice",
        "age": 20,
        "grade": "A",
        "subjects": ["Math", "Python", "English"]
    }
    
    print(f"Student info: {student}")
    
    # Accessing values
    print(f"Name: {student['name']}")
    print(f"Age: {student.get('age', 'Unknown')}")
    
    # Adding/updating values
    student["email"] = "alice@example.com"
    student["age"] = 21
    
    print(f"Updated student: {student}")
    
    # Iterating through dictionary
    print("\nStudent details:")
    for key, value in student.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()