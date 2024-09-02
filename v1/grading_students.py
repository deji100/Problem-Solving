#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    d = 0
    m = 0
    result = []
    
    for g in grades:
        d = g // 10
        m = g % 10
        
        if g < 35:
            result.append(g)
        elif m > 5:
            d = (d * 10) + 10
            if (d - g) < 3:
                result.append(d)
            else:
                result.append(g)
        else:
            d = (d * 10) + 5
            if (d - g) < 3:
                result.append(d)
            else:
                result.append(g)
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
