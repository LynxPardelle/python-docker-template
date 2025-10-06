# Python Guide for Beginners

This comprehensive guide will teach you Python fundamentals using the Docker environment. All examples can be run directly in your containerized setup!

## 🐍 What is Python?

Python is a powerful, easy-to-learn programming language created by Guido van Rossum in 1991. It's known for:

- **Simple syntax** - Reads almost like English
- **Versatile** - Web development, data science, automation, AI, and more
- **Large community** - Extensive libraries and helpful resources
- **Beginner-friendly** - Great first programming language

## 🚀 Running Python Code

In this Docker environment, you can run Python code in several ways:

```bash
# Run a specific file
make run FILE=filename.py

# Run Python commands directly
make python CMD='-c "print(\"Hello World!\")"'

# Interactive Python shell
make shell
# Then type: python
```

## 📚 Python Fundamentals

### 1. Variables and Data Types

Variables store data that can be used later in your program.

```python
# Numbers
age = 25
price = 19.99
temperature = -5

# Strings (text)
name = "Alice"
message = 'Hello World!'
paragraph = """This is a
multi-line string"""

# Booleans (True/False)
is_student = True
is_graduated = False

# None (empty/no value)
result = None
```

**Try it**: Run `make run FILE=examples/01_variables.py`

### 2. Basic Operations

```python
# Arithmetic
a = 10
b = 3

print(a + b)    # Addition: 13
print(a - b)    # Subtraction: 7
print(a * b)    # Multiplication: 30
print(a / b)    # Division: 3.333...
print(a // b)   # Floor division: 3
print(a % b)    # Modulus (remainder): 1
print(a ** b)   # Power: 1000

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenation

# Comparison
print(10 > 5)   # True
print(10 == 5)  # False
print(10 != 5)  # True
```

### 3. Data Structures

#### Lists (Ordered, Changeable)
```python
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Accessing elements (0-indexed)
print(fruits[0])    # "apple"
print(fruits[-1])   # "orange" (last element)

# Common list operations
fruits.append("grape")      # Add to end
fruits.insert(0, "mango")  # Insert at position
removed = fruits.pop()      # Remove and return last
fruits.remove("banana")     # Remove specific item

# List slicing
print(numbers[1:4])    # [2, 3, 4] (elements 1 to 3)
print(numbers[:3])     # [1, 2, 3] (first 3)
print(numbers[2:])     # [3, 4, 5] (from index 2)
```

#### Dictionaries (Key-Value pairs)
```python
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "coding", "hiking"]
}

# Accessing values
print(person["name"])           # "Alice"
print(person.get("age"))        # 30
print(person.get("job", "N/A")) # "N/A" (default if key not found)

# Modifying dictionaries
person["job"] = "Engineer"      # Add new key-value
person["age"] = 31             # Update existing
del person["city"]             # Remove key-value pair
```

#### Tuples (Ordered, Unchangeable)
```python
coordinates = (10, 20)
colors = ("red", "green", "blue")

# Accessing (like lists, but can't change)
print(coordinates[0])  # 10
x, y = coordinates     # Unpacking
```

#### Sets (Unordered, Unique values)
```python
unique_numbers = {1, 2, 3, 3, 4}  # Duplicates removed
print(unique_numbers)  # {1, 2, 3, 4}

# Set operations
numbers.add(5)         # Add element
numbers.remove(1)      # Remove element
```

### 4. Control Flow

#### If Statements
```python
age = 18

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

# Logical operators
weather = "sunny"
temperature = 75

if weather == "sunny" and temperature > 70:
    print("Perfect day for a picnic!")
elif weather == "rainy" or temperature < 50:
    print("Stay inside today")
```

#### Loops

**For Loops** (iterate over sequences):
```python
# Loop through list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# Loop through range of numbers
for i in range(5):          # 0, 1, 2, 3, 4
    print(f"Number: {i}")

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(f"Count: {i}")

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(f"Even: {i}")

# Loop with index and value
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

**While Loops** (repeat while condition is true):
```python
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1  # Same as: count = count + 1

# Be careful not to create infinite loops!
```

**Try it**: Run `make run FILE=examples/02_control_flow.py`

### 5. Functions

Functions are reusable blocks of code:

```python
# Basic function
def greet():
    print("Hello!")

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

# Function with return value
def add_numbers(a, b):
    return a + b

# Function with default parameters
def introduce(name, age=25, city="Unknown"):
    return f"Hi, I'm {name}, {age} years old, from {city}"

# Using functions
greet()                              # Hello!
greet_person("Alice")               # Hello, Alice!
result = add_numbers(5, 3)          # result = 8
info = introduce("Bob", 30)         # Uses default city
```

**Advanced Function Features**:

```python
# Variable number of arguments
def sum_all(*numbers):
    return sum(numbers)

# Keyword arguments
def create_profile(**info):
    return info

# Lambda functions (short, anonymous functions)
square = lambda x: x ** 2
multiply = lambda x, y: x * y

# Using advanced functions
total = sum_all(1, 2, 3, 4, 5)     # 15
profile = create_profile(name="Alice", age=30, job="Engineer")
squared = square(5)                 # 25
```

**Try it**: Run `make run FILE=examples/03_functions.py`

### 6. File Handling

Working with files is essential for most programs:

```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters

# Appending to a file
with open("example.txt", "a") as file:
    file.write("This line is appended.\n")
```

**JSON Files** (for structured data):
```python
import json

# Python data
data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "coding"]
}

# Write JSON file
with open("data.json", "w") as file:
    json.dump(data, file, indent=2)

# Read JSON file
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data["name"])  # Alice
```

**Try it**: Run `make run FILE=examples/04_file_handling.py`

### 7. Error Handling

Handle errors gracefully with try/except:

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("Everything went well!")
finally:
    print("This always executes")
```

### 8. Working with Libraries

Python's power comes from its vast ecosystem of libraries:

```python
# Built-in libraries
import math
import random
import datetime

print(math.pi)                      # 3.14159...
print(random.randint(1, 10))       # Random number 1-10
print(datetime.datetime.now())     # Current date/time

# External libraries (from requirements.txt)
import requests     # For web requests
import numpy as np  # For numerical computing
import pandas as pd # For data analysis

# Making web requests
response = requests.get("https://api.github.com")
print(response.status_code)  # 200

# NumPy arrays
numbers = np.array([1, 2, 3, 4, 5])
print(numbers * 2)  # [2, 4, 6, 8, 10]

# Pandas DataFrames
data = {"name": ["Alice", "Bob"], "age": [25, 30]}
df = pd.DataFrame(data)
print(df)
```

**Try it**: Run `make run FILE=examples/05_libraries.py`

## 🎯 Python Best Practices

### 1. Code Style
- Use meaningful variable names: `user_age` instead of `a`
- Follow PEP 8 style guide (Python's official style guide)
- Use comments to explain complex logic
- Keep functions small and focused

### 2. Error Handling
- Always use try/except for operations that might fail
- Be specific about which exceptions you're catching
- Provide helpful error messages

### 3. File Operations
- Always use `with` statement for file operations
- It automatically closes files even if an error occurs

### 4. Functions
- Write functions for code you use more than once
- Use descriptive function names
- Return values instead of printing when possible

## 🔄 Learning Path

### Beginner Level
1. ✅ Variables and basic data types
2. ✅ Basic operations and comparisons
3. ✅ If statements and basic loops
4. ✅ Lists and basic list operations
5. ✅ Simple functions

### Intermediate Level
6. ✅ Dictionaries and tuples
7. ✅ Advanced loops and list comprehensions
8. ✅ File reading and writing
9. ✅ Error handling
10. ✅ Working with modules

### Advanced Level
11. ✅ Object-oriented programming (classes)
12. ✅ Decorators and advanced functions
13. ✅ Working with APIs and external libraries
14. ✅ Regular expressions
15. ✅ Testing and debugging

## 🧪 Practice Exercises

### Exercise 1: Calculator
Create a simple calculator that can add, subtract, multiply, and divide:

```python
def calculator():
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operation!"
    
    return f"{num1} {operation} {num2} = {result}"

print(calculator())
```

### Exercise 2: To-Do List
Create a simple to-do list manager:

```python
todos = []

def add_todo(task):
    todos.append({"task": task, "completed": False})
    print(f"Added: {task}")

def show_todos():
    for i, todo in enumerate(todos, 1):
        status = "✓" if todo["completed"] else "○"
        print(f"{i}. {status} {todo['task']}")

def complete_todo(index):
    if 0 <= index < len(todos):
        todos[index]["completed"] = True
        print(f"Completed: {todos[index]['task']}")

# Usage
add_todo("Learn Python")
add_todo("Build a project")
show_todos()
complete_todo(0)
show_todos()
```

## 📖 Additional Resources

### Documentation
- [Official Python Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 Style Guide](https://pep8.org/)

### Practice Platforms
- [Python.org Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide)
- [Codecademy Python Course](https://www.codecademy.com/learn/learn-python-3)
- [HackerRank Python Domain](https://www.hackerrank.com/domains/python)

### Libraries to Explore
- **requests** - Web requests and APIs
- **pandas** - Data analysis and manipulation
- **matplotlib** - Creating plots and charts
- **numpy** - Numerical computing
- **beautifulsoup4** - Web scraping

## 🎉 Next Steps

Once you're comfortable with these Python fundamentals:

1. **Build projects** - Apply what you've learned
2. **Explore libraries** - Learn pandas, requests, matplotlib
3. **Learn web frameworks** - Flask or Django
4. **Data science** - Jupyter notebooks, data analysis
5. **Automation** - Script repetitive tasks

Remember: The best way to learn programming is by practicing! Start with small programs and gradually build more complex projects.

Happy coding! 🐍