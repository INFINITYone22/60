from functools import reduce

def functional_programming():
    numbers = [1, 2, 3, 4, 5]

    # Use map to square each number
    squared_numbers = list(map(lambda x: x**2, numbers))
    print("Squared numbers:", squared_numbers)

    # Use filter to get even numbers
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print("Even numbers:", even_numbers)

    # Use reduce to calculate the product of all numbers
    product = reduce(lambda x, y: x * y, numbers)
    print("Product:", product)

functional_programming()
