#!/bin/python3

import os
import sys

def push_to_stack(stack, stack_top, value, count):
    stack.append([value,count])
    stack_top += 1
    return stack, stack_top

def pop_from_stack(stack, stack_top):
    stack.pop()
    stack_top -= 1
    return stack, stack_top

# Complete the solve function below.
def solve(arr):
    n = len(arr)
 
    maximum_stack = []
    maximum_stack.append([arr[0],0]) 
    maximum_stack_top = 0
    max_paths = 0
    
    for i in range(1,n,1):
        flag = 1
        
        while((maximum_stack_top >= 0) and (flag == 1)):
            if(maximum_stack[maximum_stack_top][0] > arr[i]):
                maximum_stack, maximum_stack_top = push_to_stack(maximum_stack, maximum_stack_top, arr[i], 0)
                flag = 0
            elif(maximum_stack[maximum_stack_top][0] < arr[i]):
                maximum_stack, maximum_stack_top = pop_from_stack(maximum_stack, maximum_stack_top)
            else:
                consecutive_count = maximum_stack[maximum_stack_top][1] + 1
                max_paths += (consecutive_count)*2
                maximum_stack, maximum_stack_top = pop_from_stack(maximum_stack, maximum_stack_top)
                maximum_stack, maximum_stack_top = push_to_stack(maximum_stack, maximum_stack_top, arr[i], consecutive_count)
                flag = 0

        if(maximum_stack_top < 0):
            maximum_stack, maximum_stack_top = push_to_stack(maximum_stack, maximum_stack_top, arr[i], 0)
    
    return max_paths

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
