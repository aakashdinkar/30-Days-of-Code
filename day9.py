'''Sample Input

3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry



Sample Output

sam=99912222
Not found
harry=12299933

'''


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    dic_data = {}
    for i in range(n):
        inp_str = input().split()
        # print(inp_str[0], inp_str[1])
        dic_data[inp_str[0]] = inp_str[1]

    lines = sys.stdin.readlines()
    for item in lines:
        if item.strip() in dic_data:
            print("{}={}".format(item.strip(), dic_data[item.strip()]))
        else:
            print("Not found")
