#!/bin/python3

import os
import sys
import math

#
# Complete the downToZero function below.
#

def generate_prime_numbers(n):
    
    primes = []
    primes.append(2)

    least_divsible_prime_number = []
    least_divsible_prime_number.append(0)
    least_divsible_prime_number.append(1)

    for i in range(3,n+2,2):
        least_divsible_prime_number.append(2)
        flag = 1
        sqrt_i = math.ceil(math.sqrt(i))
        for j in range(len(primes)):
            if((i % primes[j]) == 0):
                least_divsible_prime_number.append(primes[j])
                flag = 0
                break
            
            elif(primes[j] > sqrt_i):
                break
            
            else:    
                continue
        
        if(flag == 1):
            least_divsible_prime_number.append(i)
            primes.append(i)
    
    return least_divsible_prime_number


def downToZero(n,least_divisible_prime_number):
   
   moves = 0
   
   while(n > 0):
       
       if(least_divisible_prime_number[n] == n):
           moves += 1
           n = n-1
       
       else:
           moves += 1
           n = max(least_divisible_prime_number[n],int(n/least_divisible_prime_number[n]))

#    moves += n

   return(moves)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    least_divisible_prime_number = generate_prime_numbers(1000000)
    
    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = downToZero(n,least_divisible_prime_number)

        # fptr.write(str(result) + '\n')
        print(result)

    # fptr.close()
