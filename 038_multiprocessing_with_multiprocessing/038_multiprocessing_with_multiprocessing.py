import multiprocessing
import time

def square(n):
    time.sleep(1)  # Simulate a long computation
    return n * n

def main():
    numbers = [1, 2, 3, 4, 5]

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(square, numbers)

    print("Squared numbers:", results)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
