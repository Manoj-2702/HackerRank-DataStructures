#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    sum=[]
    for row in range(len(arr)-2):
        for column in range(len(arr[row])-2):
            sum.append(arr[row][column] + arr[row][column + 1] + arr[row][column + 2] + arr[row + 1][column + 1] + arr[row + 2][column] + arr[row + 2][column + 1] + arr[row + 2][column + 2])
    
    sum.sort()
    return(max(sum))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
