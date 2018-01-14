
import sys

N = int(input())


isEven = (N % 2) == 0


if (isEven):
  if (N >= 2 and N <= 5):
    print ("Not Weird")
  elif (N >= 6 <= 20):
    print ("Weird")
  elif (N > 20):
    print ("Not Weird")
else:
  print ("Weird")
