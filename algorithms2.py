#!/bin/python

import sys

def simpleArraySum(n, ar):
    # Complete this function
    total = 0
    for i in range(n):
        total = total + ar[i]
    return total

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)

