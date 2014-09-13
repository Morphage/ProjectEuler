from math import sqrt

triangle_numbers = [0 for i in range(20000)]
triangle_numbers[0] = 1

def triangle_number(n):
    if triangle_numbers[n - 1] != 0:
        return triangle_numbers[n - 1]

    triangle_numbers[n - 1] = n + triangle_number(n - 1)
    return triangle_numbers[n - 1]

def number_of_factors(n):
    return len(set(reduce(list.__add__, 
                ([i, n / i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0))))

def euler12():
    divisors = 0
    n = 0
    
    while divisors < 500:
        n += 1
        divisors = number_of_factors(triangle_number(n))

    print triangle_number(n)

if __name__ == "__main__":
    euler12()