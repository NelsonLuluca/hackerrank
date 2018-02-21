#!/bin/python

import sys

def plusMinus(arr):
    # Complete this function
    posCount = 0.0
    negCount = 0.0
    zeroCount = 0.0
    arrLen = len(arr)
    for i in range(arrLen):
        if arr[i] > 0:
            posCount = posCount + 1
        elif arr[i] < 0:
            negCount = negCount + 1
        else:
            zeroCount = zeroCount + 1
    print posCount / arrLen
    print negCount / arrLen
    print zeroCount / arrLen

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    plusMinus(arr)

