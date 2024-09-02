#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    
    facts1 = []
    
    facts2 = []
    
    a_facts = []
    
    b_facts = []
    
    for y in range(a[-1], b[0] + 1, a[-1]):    
        for x in a:
            if y % x == 0:
                facts1.append(y)
                for z in facts1:
                    if facts1.count(z) >= len(a):
                        if z in a_facts:
                            continue
                        else:
                            a_facts.append(z) 
                
    for c in b:
        for d in a_facts:
            if c % d == 0:
                facts2.append(d)
                for e in facts2:
                    if facts2.count(e) >= len(b):
                        if e in b_facts:
                            continue
                        else:
                            b_facts.append(e)
                    
                            
                        
        
                
    return len(b_facts)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
