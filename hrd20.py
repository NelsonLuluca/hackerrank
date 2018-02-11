#!/bin/python

import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Write Your Code Here

numSwaps = 0
for i in range(0, n):
    for j in range(0,n-1):
        if (a[j] > a[j+1]):
            lval = a[j]
            rval = a[j+1]
            a[j] = rval
            a[j+1] = lval
            numSwaps = numSwaps + 1

firstElement = a[0]
lastElement = a[len(a)-1]

print("Array is sorted in %d swaps." % numSwaps)
print("First Element: %d" % firstElement)
print("Last Element: %d" % lastElement)
