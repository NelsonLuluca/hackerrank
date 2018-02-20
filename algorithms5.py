#!/bin/python

import sys

def diagonalDifference(a):
    # Complete this function
    numInputs = len(a)
    sumLeft = sumRight = 0
    for i in range(numInputs):
        sumLeft = sumLeft + a[i][i]
        sumRight = sumRight + a[i][numInputs-i-1]
    if sumRight > sumLeft:
        return abs(sumRight - sumLeft)
    else:
        return abs(sumLeft - sumRight)

if __name__ == "__main__":
    n = int(raw_input().strip())
    a = []
    for a_i in xrange(n):
        a_temp = map(int,raw_input().strip().split(' '))
        a.append(a_temp)
    result = diagonalDifference(a)
    print result

