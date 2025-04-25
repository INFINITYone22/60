import time

def cache(func):
    cached_results = {}
    def wrapper(*args):
        if args in cached_results:
            print("Returning cached result...")
            return cached_results[args]
        else:
            print("Calculating result...")
            result = func(*args)
            cached_results[args] = result
            return result
    return wrapper

@cache
def expensive_function(n):
    time.sleep(2)
    return n * 2

print(expensive_function(5))
print(expensive_function(5))
print(expensive_function(10))
