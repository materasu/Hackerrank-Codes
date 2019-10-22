#!/bin/python3

import os
import sys
import math

# Complete the solve function below.
def get_inverse_factorial(a, b, MODULUS):
    x = 1
    y = a
    while(b > 0):
        if(b%2 == 1):
            x = (x*y) % MODULUS
        y = (y*y) % MODULUS
        b = b // 2
    return x


def get_factorials(n):
    MODULUS = 1000000007
    factorials = []
    inverse_factorials = []
    factorials.append(1)
    inverse_factorials.append(1)
    for i in range(1,n+1,1):
        factorials.append((i*factorials[i-1]) % MODULUS)
        inverse_factorials.append(get_inverse_factorial(factorials[i], MODULUS-2, MODULUS))
    return(factorials, inverse_factorials)

def solve(n, m, factorials, inverse_factorials):
    MODULUS = 1000000007
    return(((factorials[n+m-2]) * (inverse_factorials[n-1] * inverse_factorials[m-1])) % MODULUS)
   

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    factorials, inverse_factorials = get_factorials(2000000)
    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m, factorials, inverse_factorials)
        print(result)
        # fptr.write(str(result) + '\n')

    # fptr.close()
