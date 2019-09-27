#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    n = len(container)
    size_of_containers = {}
    number_of_balls = {}
    
    for i in range(0,n,1):
        number_of_balls[i] = 0
    
    for i in range(0,n,1):
        for j in range(0,n,1):
            number_of_balls[j] += container[i][j]    

    for i in range(0,n,1):
        size_of_containers[sum(container[i])] = 0
        size_of_containers[number_of_balls[i]] = 0
    
    for i in range(0,n,1):
        size_of_containers[sum(container[i])] += 1
    
    for i in range(0,n,1):
        size_of_containers[number_of_balls[i]] -= 1
    
    flag = 1
    size_of_containers_keys = list(size_of_containers.keys())
    for key in size_of_containers_keys:
        if(size_of_containers[key] != 0):
            flag = 0
            break
    
    if(flag == 1):
        return("Possible")
    else:
        return("Impossible")


    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)
        print(result)
        # fptr.write(result + '\n')

    # fptr.close()
