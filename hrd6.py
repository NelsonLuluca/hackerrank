
import sys
numLines = int(raw_input())

cnt = 0
inputString = []

# read in numLines of input
while cnt < numLines:
  inputString.append(raw_input())
  cnt += 1

for i in range(0, numLines):
  # print all even characters
  for n in range(0, len(inputString[i])):
    if n % 2 == 0:
      sys.stdout.write("%s" % inputString[i][n])
  sys.stdout.write(" ")
  # print all odd characters
  for n in range(1, len(inputString[i])):
    if n % 2 <> 0:
      sys.stdout.write("%s" % inputString[i][n])
  sys.stdout.write("\n")
