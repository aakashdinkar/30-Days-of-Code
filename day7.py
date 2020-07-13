'''Sample Input

2
Hacker
Rank


Sample Output

Hce akr
Rn ak

'''


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        even_string = odd_string = ""
        string = input()
        for i in range(len(string)):
            if i % 2 != 0:
                odd_string += string[i]
            else:
                even_string += string[i]
        print(even_string, odd_string)