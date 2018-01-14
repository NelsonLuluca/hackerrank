#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

i = n
while i > 0:
  sys.stdout.write("%s " % arr[i-1])
  i -= 1
sys.stdout.write("\n")
