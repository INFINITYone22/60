def advanced_list_comprehensions():
    # Generate a list of squares of even numbers from 1 to 10
    squares_of_even = [x**2 for x in range(1, 11) if x % 2 == 0]
    print("Squares of even numbers:", squares_of_even)

    # Generate a list of tuples (x, y) where x is even and y is odd, both from 1 to 5
    even_odd_tuples = [(x, y) for x in range(1, 6) if x % 2 == 0 for y in range(1, 6) if y % 2 != 0]
    print("Even-odd tuples:", even_odd_tuples)

    # Flatten a list of lists
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened_list = [x for sublist in list_of_lists for x in sublist]
    print("Flattened list:", flattened_list)

advanced_list_comprehensions()
