#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    lst = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if (firstName.islower() and (len(firstName) <= 20) and (re.findall(r'[\w+]',firstName))) :
            if re.findall('@gmail\.com$',emailID):
                lst.append(firstName)

    lst.sort()
    for item in lst:
        print(item)
