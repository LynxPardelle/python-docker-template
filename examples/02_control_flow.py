#!/usr/bin/env python3
"""
Control Flow Examples

Learn about if statements, loops, and other control flow structures.

To run: make run FILE=examples/02_control_flow.py
"""

def main():
    print("🔄 Control Flow Examples")
    print("=" * 30)
    
    # Conditional statements
    conditional_examples()
    
    # Loop examples
    loop_examples()
    
    # Function examples
    function_examples()


def conditional_examples():
    """Examples of if, elif, and else statements"""
    print("\n🚦 Conditional Statements:")
    
    # Basic if statement
    age = 18
    if age >= 18:
        print(f"Age {age}: You are an adult!")
    else:
        print(f"Age {age}: You are a minor.")
    
    # Multiple conditions with elif
    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(f"Score {score} = Grade {grade}")
    
    # Logical operators
    weather = "sunny"
    temperature = 75
    
    if weather == "sunny" and temperature > 70:
        print("Perfect day for a picnic!")
    elif weather == "rainy" or temperature < 50:
        print("Better stay inside today.")
    else:
        print("Nice weather for a walk!")


def loop_examples():
    """Examples of for and while loops"""
    print("\n🔁 Loop Examples:")
    
    # For loop with range
    print("Counting from 1 to 5:")
    for i in range(1, 6):
        print(f"  Count: {i}")
    
    # For loop with list
    fruits = ["apple", "banana", "orange", "grape"]
    print("\nFruits in the basket:")
    for fruit in fruits:
        print(f"  🍎 {fruit}")
    
    # For loop with enumerate (get index and value)
    print("\nFruits with index:")
    for index, fruit in enumerate(fruits, 1):
        print(f"  {index}. {fruit}")
    
    # While loop
    print("\nCountdown:")
    countdown = 5
    while countdown > 0:
        print(f"  {countdown}...")
        countdown -= 1
    print("  🚀 Launch!")
    
    # List comprehension (advanced for loop)
    squares = [x**2 for x in range(1, 6)]
    print(f"\nSquares of 1-5: {squares}")


def function_examples():
    """Examples of functions"""
    print("\n🔧 Function Examples:")
    
    # Simple function
    def greet(name):
        return f"Hello, {name}!"
    
    # Function with default parameter
    def calculate_area(length, width=1):
        return length * width
    
    # Function with multiple return values
    def get_name_parts(full_name):
        parts = full_name.split()
        first_name = parts[0]
        last_name = parts[-1] if len(parts) > 1 else ""
        return first_name, last_name
    
    # Using the functions
    message = greet("Python Learner")
    print(f"Greeting: {message}")
    
    square_area = calculate_area(5)
    rectangle_area = calculate_area(5, 3)
    print(f"Square area (5x5): {square_area}")
    print(f"Rectangle area (5x3): {rectangle_area}")
    
    first, last = get_name_parts("John Doe")
    print(f"First name: {first}, Last name: {last}")


# Helper functions for examples
def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0


def fibonacci(n):
    """Generate fibonacci sequence up to n numbers"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib


if __name__ == "__main__":
    main()
    
    # Bonus examples
    print("\n🎯 Bonus Examples:")
    
    # Check even numbers from 1 to 10
    even_numbers = [num for num in range(1, 11) if is_even(num)]
    print(f"Even numbers 1-10: {even_numbers}")
    
    # Fibonacci sequence
    fib_sequence = fibonacci(8)
    print(f"First 8 Fibonacci numbers: {fib_sequence}")