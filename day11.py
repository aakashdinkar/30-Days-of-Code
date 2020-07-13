'''
Sample Input 1

5


Sample Output 1

1

Sample Input 2

13


Sample Output 2

2


Explanation

Sample Case 1:
The binary representation of  is , so the maximum number of consecutive 's is .

Sample Case 2:
The binary representation of  is , so the maximum number of consecutive 's is .

'''


#!/bin/python3

import math
import os
import random
import re
import sys

def countOnes(n):
    x = bin(n).replace("0b","").split('0')
    max_one = -1
    for item in x:
        if len(item) > max_one:
            max_one = len(item)
    return max_one


if  __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = countOnes(n)

    fptr.write(str(result) + '\n')

    fptr.close()