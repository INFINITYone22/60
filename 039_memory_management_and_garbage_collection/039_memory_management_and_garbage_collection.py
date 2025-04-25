import gc
import sys

def memory_management_and_garbage_collection():
    # Create a large list
    large_list = list(range(1000000))
    print("Size of large_list:", sys.getsizeof(large_list), "bytes")

    # Delete the list
    del large_list

    # Collect garbage
    gc.collect()

    # Get the number of unreachable objects
    print("Number of unreachable objects:", gc.collect())

memory_management_and_garbage_collection()
