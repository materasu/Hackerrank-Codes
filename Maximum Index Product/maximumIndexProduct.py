#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(arr):
    n = len(arr)
    left_maximum_indices = [0]*n
    right_maximum_indices = [0]*n
    left_maximum_stack = []
    right_maximum_stack = []
    left_maximum_stack.append([arr[0],1])
    right_maximum_stack.append([arr[n-1],n]) 
    left_maximum_stack_top = 0
    right_maximum_stack_top = 0
    
    for i in range(1,n,1):
        flag = 1
        while((left_maximum_stack_top >= 0) and (flag == 1)):
            if(left_maximum_stack[left_maximum_stack_top][0] > arr[i]):
                left_maximum_indices[i] = left_maximum_stack[left_maximum_stack_top][1]
                left_maximum_stack.append([arr[i],i+1])
                left_maximum_stack_top += 1
                flag = 0
            else:
                left_maximum_stack.pop()
                left_maximum_stack_top -= 1
        
        if(left_maximum_stack_top < 0):
            left_maximum_stack.append([arr[i],i+1])
            left_maximum_stack_top += 1
    
    for i in range(n-2,-1,-1):
        flag = 1
        while((right_maximum_stack_top >= 0) and (flag == 1)):
            if(right_maximum_stack[right_maximum_stack_top][0] > arr[i]):
                right_maximum_indices[i] = right_maximum_stack[right_maximum_stack_top][1]
                right_maximum_stack.append([arr[i],i+1])
                right_maximum_stack_top += 1
                flag = 0
            else:
                right_maximum_stack.pop()
                right_maximum_stack_top -= 1
        
        if(right_maximum_stack_top < 0):
            right_maximum_stack.append([arr[i],i+1])
            right_maximum_stack_top += 1

    max_index_product = 0
    for i in range(0,n,1):
        index_product = left_maximum_indices[i]*right_maximum_indices[i]
        if(index_product > max_index_product):
            max_index_product = index_product
    
    return max_index_product

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
