#!/usr/bin/env python3
"""
External Libraries Examples

Learn about using external Python libraries included in requirements.txt

To run: make run FILE=examples/05_libraries.py

Note: This example uses libraries from requirements.txt:
- requests (for HTTP requests)
- beautifulsoup4 (for web scraping)
- matplotlib (for plotting)
- numpy (for numerical computing)
- pandas (for data analysis)
"""

def main():
    print("📚 External Libraries Examples")
    print("=" * 30)
    
    # Check if libraries are available
    check_libraries()
    
    # Requests library examples
    requests_examples()
    
    # NumPy examples
    numpy_examples()
    
    # Pandas examples
    pandas_examples()
    
    # Matplotlib examples
    matplotlib_examples()


def check_libraries():
    """Check if required libraries are installed"""
    print("\n🔍 Checking installed libraries:")
    
    libraries = [
        ("requests", "HTTP requests"),
        ("numpy", "numerical computing"),
        ("pandas", "data analysis"),
        ("matplotlib", "plotting"),
        ("bs4", "web scraping (BeautifulSoup)")
    ]
    
    for lib_name, description in libraries:
        try:
            __import__(lib_name)
            print(f"✅ {lib_name} - {description}")
        except ImportError:
            print(f"❌ {lib_name} - Not installed")


def requests_examples():
    """Examples using the requests library"""
    print("\n🌐 Requests Library Examples:")
    
    try:
        import requests
        
        # Simple GET request to a public API
        print("Making a GET request to JSONPlaceholder API...")
        
        try:
            response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Request successful!")
                print(f"Post title: {data['title']}")
                print(f"Post body: {data['body'][:50]}...")
            else:
                print(f"❌ Request failed with status code: {response.status_code}")
        
        except requests.exceptions.RequestException as e:
            print(f"❌ Network error: {e}")
    
    except ImportError:
        print("❌ requests library not available")


def numpy_examples():
    """Examples using NumPy"""
    print("\n🔢 NumPy Examples:")
    
    try:
        import numpy as np
        
        # Creating arrays
        array1 = np.array([1, 2, 3, 4, 5])
        array2 = np.array([[1, 2, 3], [4, 5, 6]])
        
        print(f"1D array: {array1}")
        print(f"2D array:\n{array2}")
        
        # Array operations
        print(f"Array sum: {np.sum(array1)}")
        print(f"Array mean: {np.mean(array1)}")
        print(f"Array squared: {array1 ** 2}")
        
        # Creating special arrays
        zeros = np.zeros(5)
        ones = np.ones((2, 3))
        random_array = np.random.random(5)
        
        print(f"Zeros array: {zeros}")
        print(f"Ones array:\n{ones}")
        print(f"Random array: {random_array}")
        
        # Mathematical operations
        x = np.linspace(0, 10, 5)  # 5 points between 0 and 10
        y = np.sin(x)
        
        print(f"X values: {x}")
        print(f"Sin(X) values: {y}")
    
    except ImportError:
        print("❌ numpy library not available")


def pandas_examples():
    """Examples using Pandas"""
    print("\n🐼 Pandas Examples:")
    
    try:
        import pandas as pd
        import numpy as np
        
        # Creating a DataFrame
        data = {
            'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
            'Age': [25, 30, 35, 28, 32],
            'City': ['New York', 'London', 'Tokyo', 'Paris', 'Sydney'],
            'Salary': [70000, 80000, 90000, 75000, 85000]
        }
        
        df = pd.DataFrame(data)
        
        print("Sample DataFrame:")
        print(df)
        
        # Basic operations
        print(f"\nDataFrame info:")
        print(f"Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        
        # Statistical operations
        print(f"\nSalary statistics:")
        print(f"Mean salary: ${df['Salary'].mean():,.2f}")
        print(f"Max salary: ${df['Salary'].max():,.2f}")
        print(f"Min salary: ${df['Salary'].min():,.2f}")
        
        # Filtering data
        high_earners = df[df['Salary'] > 75000]
        print(f"\nHigh earners (>$75,000):")
        print(high_earners[['Name', 'Salary']])
        
        # Grouping data
        print(f"\nAverage age: {df['Age'].mean():.1f} years")
        
        # Creating a simple time series
        dates = pd.date_range('2024-01-01', periods=5, freq='D')
        ts = pd.Series(np.random.randint(1, 100, 5), index=dates)
        
        print(f"\nTime series:")
        print(ts)
    
    except ImportError:
        print("❌ pandas library not available")


def matplotlib_examples():
    """Examples using Matplotlib"""
    print("\n📊 Matplotlib Examples:")
    
    try:
        import matplotlib
        matplotlib.use('Agg')  # Use non-interactive backend for containers
        import matplotlib.pyplot as plt
        import numpy as np
        
        # Create sample data
        x = np.linspace(0, 10, 100)
        y1 = np.sin(x)
        y2 = np.cos(x)
        
        # Create a simple plot
        plt.figure(figsize=(10, 6))
        
        # Subplot 1: Line plot
        plt.subplot(2, 2, 1)
        plt.plot(x, y1, label='sin(x)', color='blue')
        plt.plot(x, y2, label='cos(x)', color='red')
        plt.title('Trigonometric Functions')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        
        # Subplot 2: Bar chart
        plt.subplot(2, 2, 2)
        categories = ['A', 'B', 'C', 'D', 'E']
        values = [23, 45, 56, 78, 32]
        plt.bar(categories, values, color='green', alpha=0.7)
        plt.title('Sample Bar Chart')
        plt.xlabel('Categories')
        plt.ylabel('Values')
        
        # Subplot 3: Histogram
        plt.subplot(2, 2, 3)
        data = np.random.normal(0, 1, 1000)
        plt.hist(data, bins=30, color='orange', alpha=0.7)
        plt.title('Normal Distribution')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        
        # Subplot 4: Scatter plot
        plt.subplot(2, 2, 4)
        x_scatter = np.random.randn(50)
        y_scatter = x_scatter + np.random.randn(50) * 0.5
        plt.scatter(x_scatter, y_scatter, color='purple', alpha=0.6)
        plt.title('Scatter Plot')
        plt.xlabel('X values')
        plt.ylabel('Y values')
        
        # Adjust layout and save
        plt.tight_layout()
        plt.savefig('sample_plots.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        print("✅ Plots created and saved as 'sample_plots.png'")
        print("   Note: In a container environment, plots are saved to files")
        
    except ImportError:
        print("❌ matplotlib library not available")
    except Exception as e:
        print(f"❌ Error creating plots: {e}")


def beautifulsoup_examples():
    """Examples using BeautifulSoup (commented out to avoid network dependencies)"""
    print("\n🕷️ BeautifulSoup Example (Web Scraping):")
    
    try:
        from bs4 import BeautifulSoup
        
        # Example with local HTML (safer for containers)
        html_content = """
        <html>
            <head><title>Sample Page</title></head>
            <body>
                <h1>Welcome to Python Learning</h1>
                <div class="content">
                    <p>This is a sample paragraph.</p>
                    <ul>
                        <li>Python</li>
                        <li>Docker</li>
                        <li>Web Scraping</li>
                    </ul>
                </div>
            </body>
        </html>
        """
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        print(f"Page title: {soup.title.text}")
        print(f"Main heading: {soup.h1.text}")
        
        # Find all list items
        items = soup.find_all('li')
        print("List items:")
        for item in items:
            print(f"  - {item.text}")
    
    except ImportError:
        print("❌ beautifulsoup4 library not available")


if __name__ == "__main__":
    main()
    
    # Bonus: BeautifulSoup example
    beautifulsoup_examples()
    
    print("\n🎯 Library Usage Tips:")
    print("1. Always check if libraries are installed before using them")
    print("2. Handle ImportError exceptions gracefully")
    print("3. Use virtual environments to manage dependencies")
    print("4. Read library documentation for best practices")
    print("5. Update requirements.txt when adding new libraries")