from math import sqrt
from math import floor

def is_prime(n):
    if n == 1: return False
    if n < 4: return True
    if n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    
    r = floor(sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    
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