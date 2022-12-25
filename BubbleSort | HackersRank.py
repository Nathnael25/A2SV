#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    totalSwap = 0
    if len(a)==1:
        print ('Array sorted in 0 swaps.')
        print ('First Element: {}'.format(a))
        print ('Last Element: {}'.format(a))
        
    else:# Write your code here
        for i in range (0,len(a)):
            for j in range (i+1,len(a)):
                if a[i]>a[j]:
                    a[i],a[j] = a[j],a[i]
                    totalSwap+= 1
        
        print ('Array is sorted in {} swaps.'.format(totalSwap))
        print ('First Element: {}'.format(a[0]))
        print ('Last Element: {}'.format(a[len(a)-1]))

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
