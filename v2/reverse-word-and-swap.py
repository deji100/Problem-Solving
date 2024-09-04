#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def convertCases(a):
    word = ""
    for x in a:
        if x.isupper():
            word += x.lower()
        else:
            word += x.upper()
    
    return word

def reverse_words_order_and_swap_cases(sentence):
    array_of_words = sentence.split()
    reversed_array_of_words = list(reversed(array_of_words))
    
    result = list(map(lambda a: convertCases(a), reversed_array_of_words))
    
    return " ".join(list(result))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
