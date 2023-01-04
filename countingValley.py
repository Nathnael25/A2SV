#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    count = 0
    count_valley = []
    r=0
    for i in range (len(path)):
        if path[i] == 'U':
            count +=1
            count_valley.append(count)
        if path[i] == 'D':
            count -=1
            count_valley.append(count)
    
    j=1        
    i=j-1
    k=j+1
    
    while (j<len(count_valley)-1):
        if count_valley[j] == 0 and ((count_valley[i]< 0 and count_valley[k]>0) or                   (count_valley[k]< 0 and count_valley[i]>0) or (count_valley[k]< 0 and                    count_valley[i]<0) or (count_valley[k]> 0 and count_valley[i]>0)):
            r+=1
            
        j+=1
    return r
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
