import time
import cProfile

def slow_function():
    result = 0
    for i in range(1000000):
        result += i
    return result

def optimized_function():
    return sum(range(1000000))

def main():
    # Profile the slow function
    cProfile.run('slow_function()', 'slow_function.prof')

    # Profile the optimized function
    cProfile.run('optimized_function()', 'optimized_function.prof')

    print("Profiling complete. Run 'python -m pstats slow_function.prof' and 'python -m pstats optimized_function.prof' to view the results.")

if __name__ == "__main__":
    main()
