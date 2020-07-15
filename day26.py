'''
Sample Input

3
12
5
7

Sample Output

Not prime
Prime
Prime
'''


#!/bin/python3

import sys
import math

def checkPrime(n):
    flag = 0
    if n < 2:
        print("Not prime")
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                flag = 1
                break
        if flag != 0:
            print("Not prime")
        else:
            print("Prime")

n = int(input())
for _ in range(n):
    inp = int(input())
    checkPrime(inp)