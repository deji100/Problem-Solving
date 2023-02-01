#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    
    a_f = 0
    o_f = 0

    for x in range(0, len(apples)):
        if apples[x] < 0:
            if a - abs(apples[x]) in range(s, t+1):
                a_f += 1
        else:
            if a + apples[x] in range(s, t+1):
                a_f += 1
                
    for z in range(0, len(oranges)):
        if oranges[z] < 0:
            if b - abs(oranges[z]) in range(s, t+1):
                o_f += 1
        else:
            if b + oranges[z] in range(s, t+1):
                o_f += 1
            
    print(a_f)
    print(o_f)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    
    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
