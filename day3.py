'''Sample Input

12.00
20
8

Sample Output

15'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    total = 0
    total += meal_cost
    total += meal_cost * tip_percent/100
    total += meal_cost * tax_percent/100
    print(round(total))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)