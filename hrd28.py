#!/bin/python

import sys
import re

a = list()
N = int(raw_input().strip())
regStr = "^([a-zA-Z0-9_\-\.]+)@gmail\.com$"
for a0 in xrange(N):
    firstName,emailID = raw_input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if re.search(regStr, emailID, flags=0):
        #print(firstName)
        a.append(firstName)

#print "LIST"
#print a
sortedList = sorted(a)
#print "SORTED"
#print sortedList
for i in range(len(sortedList)):
    print(sortedList[i])