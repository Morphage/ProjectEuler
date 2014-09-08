def euler5():
    n = 20
    found = False

    while not found:
        found = True

        for i in range(11,21):
            if n % i != 0:
                found = False
                n += 20
                break

    return n

if __name__ == "__main__":
    print euler5()