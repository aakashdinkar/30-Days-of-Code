'''Sample Input 0

3

Sample Output 0

3


Sample Input 1

za

Sample Output 1

Bad String'''


#!/bin/python3

import sys


S = input().strip()
try:
    string_int = int(S)
    print(string_int)
except:
    print("Bad String")