import numpy as np

def numpy_array_operations():
    # Create two NumPy arrays
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([[7, 8, 9], [10, 11, 12]])

    # Perform element-wise addition
    addition = arr1 + arr2
    print("Element-wise addition:\n", addition)

    # Perform element-wise multiplication
    multiplication = arr1 * arr2
    print("Element-wise multiplication:\n", multiplication)

    # Calculate the mean of each array
    mean1 = np.mean(arr1)
    mean2 = np.mean(arr2)
    print("Mean of arr1:", mean1)
    print("Mean of arr2:", mean2)

    # Reshape the arrays
    reshaped_arr1 = arr1.reshape((3, 2))
    print("Reshaped arr1:\n", reshaped_arr1)

numpy_array_operations()
