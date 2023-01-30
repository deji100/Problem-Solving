#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    result = []
    alice = 0
    bob = 0
    for x in range(0, len(a)):
        if x == 0:
            if a[x] > b[x]:
                alice += 1
            elif a[x] < b[x]:
                bob += 1                
            else:
                continue
        elif x == 1:
            if a[x] > b[x]:
                alice += 1
            elif a[x] < b[x]:
                bob += 1                
            else:
                continue
        else:
            if a[x] > b[x]:
                alice += 1
            elif a[x] < b[x]:
                bob += 1                
            else:
                continue
    result = [alice, bob]
    
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
