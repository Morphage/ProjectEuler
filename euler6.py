def euler6():
    sum_of_squares = 0
    sum = 0
    
    for i in range(1, 101):
        sum_of_squares += i * i
        sum += i
    
    print sum * sum - sum_of_squares

if __name__ == '__main__':
    euler6()