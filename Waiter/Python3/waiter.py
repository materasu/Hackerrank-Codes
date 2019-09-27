#!/bin/python3

import os
import sys
import math

#
# Complete the waiter function below.
#

def generate_prime_numbers(n,q):
    
    prime_count = 1
    primes = []
    primes.append(2)

    least_divsible_prime_position = []
    least_divsible_prime_position.append(-1)
    least_divsible_prime_position.append(-1)

    for i in range(3,n+1,2):
        least_divsible_prime_position.append(1)
        flag = 1

        for j in range(len(primes)):
            if((i % primes[j]) == 0):
                least_divsible_prime_position.append(min(j+1,q+1))
                flag = 0
                break
            
            elif(primes[j] > math.ceil(math.sqrt(i))):
                break
            
            else:    
                continue
        
        if(flag == 1):
            prime_count += 1
            least_divsible_prime_position.append(min(prime_count,q+1))
            primes.append(i)
    
    return least_divsible_prime_position
            




def waiter(number, q):
   
   n = len(number)
   least_divsible_prime_position = generate_prime_numbers(10000,q)

   b = {}
   a_q = []

   for i in range(1,q+1):
        b[i] = []
   
   for i in range(n-1,-1,-1):
       least_divisible_prime = least_divsible_prime_position[number[i]]
       
       if(least_divisible_prime > q):
            a_q.append(number[i])
       
       else:
            b[least_divisible_prime].append(number[i])

   print(b)
   print(a_q)
   
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
    print(result)
