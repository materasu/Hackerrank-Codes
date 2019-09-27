#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(n, shots, m, players):

    shots_started = {}
    shots_ended = {}
    result = 0

    for i in range(0,n,1):
        shot = shots[i]
        shots_started[shot[0]] = 0
        shots_ended[shot[1]+1] = 0

    for i in range(0,m,1):
        player = players[i]
        shots_started[player[0]] = 0
        shots_started[player[1]] = 0
        shots_ended[player[0]] = 0 
        shots_ended[player[1]] = 0
    
    shots_started_keys = list(shots_started.keys())
    shots_ended_keys = list(shots_ended.keys())
    
    shots_started_keys.sort()
    shots_ended_keys.sort()

    shots_started_length = len(shots_started_keys)
    shots_ended_length = len(shots_ended_keys)

    for i in range(0,n,1):
        shot = shots[i]
        shots_started[shot[0]] += 1
        shots_ended[shot[1]+1] += 1 

    for i in range(1,shots_started_length,1):
        shots_started[shots_started_keys[i]] += shots_started[shots_started_keys[i-1]]
    
    for i in range(1,shots_ended_length,1):
        shots_ended[shots_ended_keys[i]] += shots_ended[shots_ended_keys[i-1]]

    for i in range(0,m,1):
        player = players[i]
        result += shots_started[player[0]] - shots_ended[player[0]]
        result += shots_started[player[1]] - shots_started[player[0]]

    # print(shots_started)
    # print(shots_ended)

    return result

if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    shots = []

    for _ in range(n):
        shots.append(list(map(int, input().rstrip().split())))

    players = []

    for _ in range(m):
        players.append(list(map(int, input().rstrip().split())))

    result = solve(n, shots, m, players)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
