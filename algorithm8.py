#!/bin/python

import sys

def miniMaxSum(arr):
    # Complete this function
    n = len(arr)
    counts = []

    for i in range(n):
        counts.append(0)
        for j in range(n):
            if j != i:
                counts[i] = counts[i] + arr[j]
        if i == 0:
            theMin = counts[i]
            theMax = counts[i]
        elif counts[i] < theMin:
            theMin = counts[i]
        elif counts[i] > theMax:
            theMax = counts[i]
    print("%d %d" % (theMin, theMax))

if __name__ == "__main__":
    arr = map(int, raw_input().strip().split(' '))
    miniMaxSum(arr)


