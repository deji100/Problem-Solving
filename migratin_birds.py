#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    
    max_birds = {}
    max_value = {}
    max_key = None
    
    for x in arr:
        if x in max_birds:
            max_birds[x] += 1
        else:
            max_birds[x] = 1
            
    for k,v in max_birds.items():
        if not max_key == None:
            if max_birds[max_key] == v:
                max_value[k] = v
                max_key = k
            elif max_birds[max_key] < v:
                max_value[k] = v
                if max_key in max_value:
                    del max_value[max_key]
                max_key = k
        else:
            max_key = k
    
    if len(max_value) > 1:
        return min(max_value)
    else:
        return max(max_value)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
