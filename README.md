# merge-conflict-practice

## Introduction
To practice how to resolve merge conflict, I made an example code that can occur conflict.    
I made 2 branches. One branch is calculator.py that added multiply function, the other is modulo function.    
Each codes modified same lines and had different contents.    
Using these, I added, committed, branched and push.    
I noted these contents on this README.md.    

## Initial source code
```
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


# main function
def main():
    print("Simple Calculator Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Choose an operation (1/2/3/4): ") 
    
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
    else:
        print("wrong input, please try again.")

if __name__ == "__main__":
    main()
```
This source code is simple calculator using 2 numbers.   
I will add some functions in this code.   
While doing this process, I will make some conflicts and practice how to control it.    

## Directory
In the local, I make a folder to put source code(calculator.py) and .git together.
```
├─merge-practice-conflict
│      calculator.py
│      .git
```

## Make main branch
![Image](https://github.com/user-attachments/assets/46a1bc01-c9fe-47c1-8605-1701076602e2)    
First, I made a main branch and committed, push source code to branch.
```
git init                                                                      # initialize
git add calculator.py                                                         # add source code
git commit -m "initial calculator"                                            # commit
git branch -M main                                                            # make main branch
git remote and origin https://github.com/sdy1804/merge-conflict-practice.git  # connect remote to repository
git push -u origin main                                                       # push code to branch
```

## Make second branch (feature-power)
![Image](https://github.com/user-attachments/assets/cdfbddb7-e39e-401f-b28b-224419bab63f)    
And then, I made a second branch to upload addtional version of source code.    
I added multiply function to calculator.py.    
    
This is version of adding multiply function.    
```
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
    """Power function"""
    return a ** b


# main function
def main():
    print("Simple Calculator Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power") # Added power operation
    
    
    choice = input("Choose an operation (1/2/3/4/5): ")  # Added number 5
    
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
    elif choice == '5':  # Added power operation
        print(f"result: {power(num1, num2)}")
    else:
        print("wrong input, please try again.")

if __name__ == "__main__":
    main()
```
I added source code which is version of adding multiply function and committed, push it.    

## Make third branch (feature-mod)
![Image](https://github.com/user-attachments/assets/ec6ff577-4d52-4626-ae02-bae222691997)    
I made a third branch to make conflict as well.    
Third version of source code has modulo function.    
The code lines that added modulo function is the same as lines that added multiply function in the second branch.    
    
This is version of adding modulo function.     
```
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

def modulo(a, b):
    """Return the remainder of a divided by b"""
    if b == 0:
        return "You cannot divide by zero!"
    return a % b


# main function
def main():
    print("Simple Calculator Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo") # occur conflict!
    
    choice = input("Choose an operation (1/2/3/4/5): ") # it can also occur conflict
    
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
    elif choice == '5':  # occur conflict!
        print(f"result: {modulo(num1, num2)}")
    else:
        print("wrong input, please try again.")

if __name__ == "__main__":
    main()
```

## Control conflict
I tried to merge each branches into main branch.    
As I intended conflict is occured, I could see warning in gitbash.    
![Image](https://github.com/user-attachments/assets/1f8c5e27-83d1-4ea0-9d80-7c7e8cc0e0f8)    

And I checked source code, I could see the screen as follow.    
![Image](https://github.com/user-attachments/assets/3a3b1c8e-7124-48a5-ab87-f663788a4554)    

To control conflict, I had to delete some symbols such as '====', '<<<', '>>>'.    
And I had to choose whether delete code line or not.    
If I want to use both codes lines, just leave all codes.    
Or I can delete specific code that will not use and remain other codes to use.    
After I modified codes, save it.    
And just add, commit and push again to main branch.    
![Image](https://github.com/user-attachments/assets/51ff371a-463f-4107-b768-3670d26857e8)    
You can check results on this repo.    
