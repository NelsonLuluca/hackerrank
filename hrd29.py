#!/bin/python

import sys

def maxAnd(n,k):
    maxVal = 0
    print("checking n=%d k=%d" % (n,k))

    for i in range(1,n+1):
        for j in range(i+1,n+1):
            bitand = i & j
            print("bit=%d i=%d j=%d" % (bitand, i, j))
            if bitand > maxVal and bitand < k:
                maxVal = bitand
    #print(maxAnd)
    return(maxVal)

t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    print(maxAnd(n,k))  

