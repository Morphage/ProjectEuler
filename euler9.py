from math import sqrt

def euler9():
    for n in range(1,25):
        for m in range(n,25):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            
            if a + b + c == 1000:
                return a * b * c

if __name__ == "__main__":
    print euler9()