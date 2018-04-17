#!/bin/python3
#https://www.hackerrank.com/challenges/time-conversion/problem

import os
import sys
from functools import reduce
#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    strDay  = s[-2:]
    arrTime = list(map(int, s[:-2].split(':')))

    if(strDay == 'PM'):
        if(arrTime[0] != 12):
            arrTime[0] += 12
    elif(strDay == 'AM'):
        if(arrTime[0] == 12):
            arrTime[0] = 0
    return reduce(lambda x, y: str(x).zfill(2)+':'+str(y).zfill(2), arrTime)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

