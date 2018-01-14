
import sys
numLines = int(raw_input())

cnt = 0
inputString = []
tel = {}

# read in numLines of input
while cnt < numLines:
  inputString = raw_input().split(" ")
  tel[inputString[0]] = inputString[1]
  cnt += 1

#print("sam phone number is: %s" % tel['sam'])


inputString = raw_input()
while (inputString <> ''):
  if (inputString in tel):
    print("%s=%s" % (inputString, tel[inputString]))
  else:
    print("Not found")
  try:
    inputString = raw_input()
  except EOFError:
    inputString = ''
