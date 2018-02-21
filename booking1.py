#!/bin/python

import sys


# Complete the function below.

def best_hotels():
    return 0


n = int(raw_input().strip())
a = []
b = []
# read hotel ids & scores into separte arrays
for i in range(n):
    myList = raw_input().strip().split(' ')
    #print(myList)
    # found the hotelID, so updating
    if (int(myList[0]) in a):
        #print ("updating hotel ID")
        m = a.index(int(myList[0]))
        b[m] = myList[1]
    # this is a new hotelID
    else:
        #print ("new hotel ID")
        a.append(int(myList[0]))
        b.append(int(myList[1]))

# bubble sort the arrays
newLen = len(a)
for i in range(newLen-1):
    for j in range(newLen-1):
        # bubble sort - swap values
        lval = a[j]
        lhotel = b[j]
        rval = a[j+1]
        rhotel = b[j+1]
        if lhotel > rhotel:
            a[j] = rval
            a[j+1] = lval
            b[j] = rhotel
            b[j+1] = lhotel

for i in range(len(a)):
    print (a[i])
    #print("ID: %d SCORE: %d" % (int(a[i]),int(b[i])))
