#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    p_d = []
    s_d = []
    count_to_r = 0
    count_to_l = len(arr)
    result = None
    
    for x in arr:
        if x == 0:
            p_d.append(x[0])
            s_d.append(x[len(x) - 1])
        elif x == len(arr) - 1:
            p_d.append(x[len(x) - 1])
            s_d.append(x[0])
        else:
            count_to_r += 1
            count_to_l -= 1
            p_d.append(x[count_to_r - 1])
            s_d.append(x[count_to_l])
    result = sum(p_d) - sum(s_d)
    return abs(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
