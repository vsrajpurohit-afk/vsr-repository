# Simple Python program to add two numbers

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = add_numbers(num1, num2)
    print("The sum is:", result)
