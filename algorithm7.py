#!/bin/python

import sys

def staircase(n):
    # Complete this function
    for i in range (n): 
        for j in range (n-1, -1, -1):
            #print("i: %d j: %d n: %d" % (i, j, n))
            if j > i:
                sys.stdout.write(" ")
            else:
                sys.stdout.write("#")
        sys.stdout.write("\n")

if __name__ == "__main__":
    n = int(raw_input().strip())
    staircase(n)

