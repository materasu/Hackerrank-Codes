#!/bin/python3

import os
import sys
import math

#
# Complete the lights function below.
#



def lights(n):
    MODULUS = 100000
    answer = 2**n - 1
    answer = int(answer) % MODULUS
    return answer


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = lights(n)
        print(result)
        # fptr.write(str(result) + '\n')

    # fptr.close()
