#!/bin/python3
#https://www.hackerrank.com/challenges/birthday-cake-candles/problem

import os
import sys
from functools import reduce

#
# Complete the birthdayCakeCandles function below.
#
def birthdayCakeCandles(n, ar):
    #
    # Write your code here.
    #
    arrSort = sorted(ar,reverse=True)
    resultArr = [x for x in arrSort if x == arrSort[0]]
    return(len(resultArr))
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(n, ar)

    f.write(str(result) + '\n')

    f.close()

