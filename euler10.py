from prime_library import next_prime

def euler10():
    sum = 0
    prime = 2

    while prime < 2000000:
        sum += prime
        prime = next_prime(prime)
    
    return sum

if __name__ ==  "__main__":
    print euler10()