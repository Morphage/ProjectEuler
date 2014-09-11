from math import sqrt

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    if n % 2 == 0:
        n += 1
    else:
        n += 2

    while not is_prime(n):
        n += 2

    return n

def prime_factors(n):
    factors = []
    prime = 2

    while n != 1:
        if n % prime == 0:
            factors.append(prime)
            n /= prime
        else:
            prime = next_prime(prime)

    return factors