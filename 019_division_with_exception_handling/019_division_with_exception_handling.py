def divide(x, y):
    try:
        result = x / y
        print("Result:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print("Invalid input. Please enter numbers.")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

divide(num1, num2)
