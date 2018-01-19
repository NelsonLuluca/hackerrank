
import sys

i = 1
for line in sys.stdin:
    print line
    if (i <> 1):
        nums = line.split()
        mins[i] = nums[0]
        deadlines[i] = nums[1]
        print ("line %d minutes %d deadlines %d" % (i, mins[i], deadlines[i]))
    i += 1
       
