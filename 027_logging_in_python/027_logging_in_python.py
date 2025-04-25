import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def divide(x, y):
    try:
        result = x / y
        logging.info(f"Divided {x} by {y} = {result}")
        return result
    except ZeroDivisionError:
        logging.error(f"Tried to divide {x} by zero")
        return None

num1 = 10
num2 = 0

divide(num1, num2)
