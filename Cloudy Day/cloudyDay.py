#!/bin/python3

import math
import os
import random
import re
import sys


def maximumPeople(n, p, x, m, y, r):
    
    position_info = {}
    population_info = {}
    cloud_or_town = {}
    result = 0

    for i in range(0,m,1):
        position_info[y[i]-r[i]] = 0
        position_info[y[i]+r[i]+1] = 0
        population_info[y[i]-r[i]] = 0
        population_info[y[i]+r[i]+1] = 0
        cloud_or_town[y[i]-r[i]] = -1
        cloud_or_town[y[i]+r[i]+1] = -1
        

    for i in range(0,n,1):
        position_info[x[i]] = 0
        population_info[x[i]] = 0
        cloud_or_town[x[i]] = 1

    for i in range(0,m,1):
        position_info[y[i]-r[i]] += 1
        position_info[y[i]+r[i]+1] -= 1
    
    position_info_keys = list(position_info.keys())
    position_info_keys.sort()
    position_info_length = len(position_info_keys)

    for i in range(1,position_info_length,1):
        position_info[position_info_keys[i]] += position_info[position_info_keys[i-1]] 
    
    for i in range(0,n,1):
        if(position_info[x[i]] == 0):
            population_info[x[i]] += p[i]
            result += p[i]
        elif(position_info[x[i]] == 1):
            population_info[x[i]] += p[i]
        else:
            continue
    
    population_info_keys = list(population_info.keys())
    population_info_keys.sort()
    population_info_length = len(population_info_keys)
    
    for i in range(1,population_info_length,1):
        population_info[population_info_keys[i]] += population_info[population_info_keys[i-1]]

    max_result = result

    for i in range(0,m,1):
        extra = population_info[y[i]+r[i]+1] - population_info[y[i]-r[i]]
        extra_result = extra + result
        if(extra_result > max_result):
            max_result = extra_result
        else:
            continue
    
    return max_result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(n, p, x, m, y, r)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
