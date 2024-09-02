#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    v = scores[0]
    mx = 0
    mn = 0
    
    for x in range(0, len(scores)):
        if not x == len(scores) - 1:
            if scores[x+1] > v:
                v = scores[x+1]
                mx += 1
            elif scores[x] == scores[x+1]:
                continue
            else:
                continue
        else:
            break
            
    for y in range(0, len(scores)):
        if not y == len(scores) - 1:
            if v < scores[y+1]:
                continue
            elif scores[y] == scores[y+1]:
                continue
            else:
                if scores[0] < scores[y+1]:
                    continue
                elif scores[0] == scores[y+1]:
                    v = scores[y+1]
                elif scores[y+1] < scores[0]:
                    v = scores[y+1]
                    mn += 1
                else:
                    v = scores[y+1]
                    mn += 1
        else:
            break
            
    return [mx, mn]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
