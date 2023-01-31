#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    time = ""
    if s[-2:] == "AM":
        if s[:2] == "12":
            time = "00" + s[2:8]
        else:
            time = s[:8]
    else:
        if s[:2] == "12":
            time = s[:8]
        else:
            time = str(int(s[:2]) + 12) + s[2:8]
    return time
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
