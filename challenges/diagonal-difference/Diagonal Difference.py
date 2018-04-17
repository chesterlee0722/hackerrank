#!/bin/python3
#https://www.hackerrank.com/challenges/diagonal-difference/problem

import os
import sys
#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a):
    #
    # Write your code here.
    #
    
    absSum = sum(oneList[index] - oneList[-index-1] for index,oneList in enumerate(a))
    return abs(absSum)



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input())
    
    a = []
    
    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

f.write(str(result) + '\n')

f.close()

