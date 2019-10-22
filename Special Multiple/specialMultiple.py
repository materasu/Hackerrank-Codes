#!/bin/python3

import os
import sys

# Complete the solve function below.
def make_numbers(n, numbers, digit_count, DIGIT_UPPER_LIMIT):
    if(digit_count >= DIGIT_UPPER_LIMIT):
        return numbers
    else:
        n *= 10
        numbers.append(n)
        numbers = make_numbers(n, numbers, digit_count+1, DIGIT_UPPER_LIMIT)
        n += 9
        numbers.append(n)
        numbers = make_numbers(n, numbers, digit_count+1, DIGIT_UPPER_LIMIT)
        return numbers

def solve(n, numbers):
    print(len(numbers))
    answer = 0
    for number in numbers:
        if((number % n) == 0):
            answer = number
            break
    return answer

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    numbers = []
    numbers.append(9)
    numbers = make_numbers(9, numbers, 1, 10)
    numbers.sort()
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n, numbers)
        print(result)
        # fptr.write(result + '\n')

    # fptr.close()
