import sys


arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

numrows = len(arr)
numcols = len(arr[0])
glassTotal = 0
glassMax = -63
for i in range(numrows-2):
   for j in range(numcols-2):
#      print("ROW: %d COL: %d VAL: %d" % (arr_i, arr_j, arr[arr_i][arr_j]))
      glassTotal = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
      if glassTotal > glassMax:
         glassMax = glassTotal
      print("CURRENT glassTotal: %d" % glassTotal)

print(glassMax)
