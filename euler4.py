def reverse(n):
    rev = 0
    
    while n != 0:
        rev = rev * 10 + n % 10
        n /= 10

    return rev

def is_palindrome(n):
    return n == reverse(n)

def euler4():
    largest = 0

    for x in range(999, 900, -1):
        for y in range(x, 900, -1):
            n = x * y
            if is_palindrome(n) and n > largest:
                largest = n
    
    print largest

if __name__ == "__main__":
    euler4()