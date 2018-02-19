#!/bin/python

import sys

def aVeryBigSum(n, ar):
    # Complete this function
    # python handles long ints implicitely!
    result = 0
    for i in range(n):
        result = result + ar[i]
    return result

n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)

