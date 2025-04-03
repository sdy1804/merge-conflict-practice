# calculator.py (main branch)
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        return "You cannot divide by zero!"
    return a / b

def power(a, b):
    """Raise a to the power of b"""
    return a ** b


# main function
def main():
    print("Simple Calculator Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power") # added in new branch
    
    choice = input("Choose an operation (1/2/3/4/5): ") # modified 
    
    num1 = float(input("input first number: "))
    num2 = float(input("input second number: "))
    
    if choice == '1':
        print(f"result: {add(num1, num2)}")
    elif choice == '2':
        print(f"result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"result: {divide(num1, num2)}")
    elif choice == '5':  # added in new branch
        print(f"result: {power(num1, num2)}")
    else:
        print("wrong input, please try again.")

if __name__ == "__main__":
    main()