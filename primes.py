"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(num):
    count = 0
    for i in range(2,int(num/2)+1,1):
        if num % i == 0:
            count += 1
    return count


def primes(number_of_primes):
    list = []
    count = 0
    i = 1
    if number_of_primes <1:
        raise ValueError("The number of primes should be greater than zero")
    while count< number_of_primes:
        i += 1
        if isPrime(i) < 1:
            list.insert(count,i)
            count += 1
    return list
