def prime_generator(limit):
    number = 2
    while number < limit:
        if is_prime(number):
            yield number
        number += 1

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

limit = int(input("Enter the limit: "))
primes = prime_generator(limit)

for prime in primes:
    print(prime)
