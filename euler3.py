from prime_library import prime_factors

def euler3():
    n = 600851475143
    print prime_factors(n)[-1]

if __name__ == "__main__":
    euler3()