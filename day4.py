'''Sample Input 0

3

Sample Output 0

Weird

Sample Input 1

24

Sample Output 1

Not Weird'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N % 2 != 0:
        print("Weird")
    if N % 2 == 0:
        if N >= 2 and N <= 5:
            print("Not Weird")
        elif N >= 6 and N <= 20:
            print("Weird")
        else:
            print("Not Weird")
