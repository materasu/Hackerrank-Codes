#!/bin/python3

import os
import sys

# Complete the solve function below.
def get_gcd(a, b):
    if(b == 0):
        return a
    return get_gcd(b, a%b)

def solve(a, b, c):
    gcd = get_gcd(a, b)
    if((c <= max(a,b)) and (c % gcd) == 0):
        print(gcd)
        return "YES"
    else:
        print(gcd)
        return "NO"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        abc = input().split()

        a = int(abc[0])

        b = int(abc[1])

        c = int(abc[2])

        result = solve(a, b, c)
        print(result)
        # fptr.write(result + '\n')

    # fptr.close()
