#!/usr/bin/python3

def isPrime(n):
    if n == 1:
        print("1 is a special.")
        return False
    for x in range(2,n):
        if n % x == 0:
            print("{} equals {} X {}, Therefore, {} is not a prime number.".format(n, x, n//x, n))
            return False
    else:
        print(n, "is a prime number.")
        return True

for n in range(1,20):
    isPrime(n)