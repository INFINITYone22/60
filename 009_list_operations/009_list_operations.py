def list_operations(numbers):
    if not numbers:
        return None, None, None

    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / len(numbers)

    return maximum, minimum, average

numbers = [float(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
maximum, minimum, average = list_operations(numbers)

if maximum is not None:
    print("Maximum:", maximum)
    print("Minimum:", minimum)
    print("Average:", average)
else:
    print("The list is empty.")
