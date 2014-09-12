from prime_library import next_prime

def euler7():    
    prime = 2

    for i in range(1,10001):
        prime = next_prime(prime)
    
    return prime

if __name__ ==  "__main__":
    print euler7()