#!/bin/python3

import os
import sys

# Complete the solve function below.

def solve(n, m):
    MODULUS = 1000000007
    total_digits = n + (m - 1) # (m - 1) because first element has to be one
    answer = 1
    total_digits_iter = 1
    n_iter = 1
    m_iter = 1
    denominator_overflow = 1
    while(total_digits_iter <= total_digits):
        if(n_iter <= n):
            print("Total Digits Iterator = ", total_digits_iter)
            print("N Iterator = ", n_iter)
            answer *= int(total_digits_iter // n_iter)
            total_digits_iter += 1
            n_iter += 1
            print("Answer = ", answer)
        else:
            print("Total Digits Iterator = ", total_digits_iter)
            print("M Iterator = ", m_iter) 
            answer = (answer * total_digits_iter)
            denominator_overflow = (denominator_overflow * m_iter)
            if((answer % denominator_overflow) == 0):
                answer = answer // denominator_overflow 
                denominator_overflow = 1
            else:
                pass
            total_digits_iter += 1
            m_iter += 1
            print("Answer = ", answer)
    print("Out of Loop Answer = ", answer)
    print("Denominator Overflow = ", denominator_overflow)
    answer = (answer // denominator_overflow) % MODULUS

    return answer


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m)

        print(result)
        # fptr.write(str(result) + '\n')

    # fptr.close()
