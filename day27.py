#!/bin/python3

import math
import os
import random
import re
import sys

def fineCalculator(due_date, returned_date):
    if due_date[2] == returned_date[2]:
        if due_date[1] == returned_date[1]:
            if returned_date[0] <= due_date[0]:
                return 0
            else:
                return 15*(returned_date[0] - due_date[0])
        elif due_date[1] > returned_date[1]:
            return 0
        else:
            return 500*(returned_date[1] - due_date[1])
    elif due_date[2] > returned_date[2]:
        return 0
    return 10000


returned_date = list(map(int, input().split()))
due_date = list(map(int, input().split()))
fine = fineCalculator(due_date, returned_date)
print(fine)