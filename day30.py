'''
Sample Input

3
5 2
8 5
2 2

Sample Output

1
4
0
'''


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        if (k-1 | k) > n and k % 2 == 0:
            print(k-2)
        else:
            print(k-1)da