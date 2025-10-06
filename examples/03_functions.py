#!/usr/bin/env python3
"""
Functions and Modules Examples

Learn about creating and using functions, and organizing code into modules.

To run: make run FILE=examples/03_functions.py
"""

def main():
    print("🔧 Functions and Modules Examples")
    print("=" * 35)
    
    # Basic functions
    basic_function_examples()
    
    # Advanced function features
    advanced_function_examples()
    
    # Working with modules
    module_examples()


def basic_function_examples():
    """Examples of basic function concepts"""
    print("\n📝 Basic Functions:")
    
    # Function without parameters
    def say_hello():
        return "Hello, World!"
    
    # Function with parameters
    def add_numbers(a, b):
        return a + b
    
    # Function with default parameters
    def introduce(name, age=25, city="Unknown"):
        return f"Hi, I'm {name}, {age} years old, from {city}"
    
    # Using the functions
    print(f"Simple function: {say_hello()}")
    print(f"Addition: {add_numbers(5, 3)}")
    print(f"Introduction 1: {introduce('Alice')}")
    print(f"Introduction 2: {introduce('Bob', 30)}")
    print(f"Introduction 3: {introduce('Charlie', 28, 'New York')}")


def advanced_function_examples():
    """Examples of advanced function features"""
    print("\n🚀 Advanced Function Features:")
    
    # Function with *args (variable number of arguments)
    def sum_all(*numbers):
        return sum(numbers)
    
    # Function with **kwargs (keyword arguments)
    def create_profile(**kwargs):
        profile = {}
        for key, value in kwargs.items():
            profile[key] = value
        return profile
    
    # Function with both *args and **kwargs
    def flexible_function(*args, **kwargs):
        result = f"Args: {args}, Kwargs: {kwargs}"
        return result
    
    # Lambda functions (anonymous functions)
    square = lambda x: x ** 2
    multiply = lambda x, y: x * y
    
    # Using advanced functions
    print(f"Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")
    
    profile = create_profile(name="Alice", age=30, job="Engineer", city="Boston")
    print(f"Profile: {profile}")
    
    flex_result = flexible_function(1, 2, 3, name="test", value=42)
    print(f"Flexible function: {flex_result}")
    
    print(f"Lambda square of 5: {square(5)}")
    print(f"Lambda multiply 3*4: {multiply(3, 4)}")
    
    # Higher-order functions
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(square, numbers))
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    print(f"Original: {numbers}")
    print(f"Squared: {squared_numbers}")
    print(f"Even only: {even_numbers}")


def module_examples():
    """Examples of working with modules"""
    print("\n📦 Module Examples:")
    
    # Built-in modules
    import math
    import random
    import datetime
    from collections import Counter
    
    # Math module
    print(f"Pi: {math.pi:.4f}")
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"Ceiling of 4.3: {math.ceil(4.3)}")
    
    # Random module
    print(f"Random number 1-10: {random.randint(1, 10)}")
    print(f"Random choice from list: {random.choice(['apple', 'banana', 'cherry'])}")
    
    # Datetime module
    now = datetime.datetime.now()
    print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Collections module
    fruits = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
    fruit_count = Counter(fruits)
    print(f"Fruit count: {fruit_count}")


# Decorator examples
def timer_decorator(func):
    """A simple decorator to time function execution"""
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    
    return wrapper


@timer_decorator
def slow_function():
    """A function that takes some time to execute"""
    import time
    time.sleep(0.1)  # Sleep for 0.1 seconds
    return "Function completed!"


# Recursion example
def factorial(n):
    """Calculate factorial using recursion"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci_recursive(n):
    """Calculate nth fibonacci number using recursion"""
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == "__main__":
    main()
    
    # Bonus examples
    print("\n🎯 Bonus Examples:")
    
    # Decorator example
    result = slow_function()
    print(f"Slow function result: {result}")
    
    # Recursion examples
    print(f"Factorial of 5: {factorial(5)}")
    print(f"5th Fibonacci number: {fibonacci_recursive(5)}")
    
    # Scope example
    global_var = "I'm global"
    
    def scope_example():
        local_var = "I'm local"
        print(f"Inside function - Global: {global_var}")
        print(f"Inside function - Local: {local_var}")
    
    scope_example()
    print(f"Outside function - Global: {global_var}")
    # print(local_var)  # This would cause an error!