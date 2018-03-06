
# solve voltaiq code challenge
# given a string of numbers (digits)
# read them out to get the next line
# 1 reads one 1
# 11 reads 2 1 (literally two ones)
# 21 reads 1 2 1 1
# etc etc
def getHeadStr(ar):
    retStr = ""
    n = 1
    fchar = ar[0]
    arlen = len(ar)
    done = False
    while n < arlen and done == False:
        if (ar[n] == fchar):
            n = n + 1
        else:
            done = True
    retStr +=str(n)
    retStr +=str(fchar)
    if len(ar) > n:
        retStr += getHeadStr(ar[n:])
    return retStr

# we'll start with a string of "1"
myStrings = ["1"]

# we'll iterate on 10 levels of the game
for i in range(10):
    myStrings.append(getHeadStr(myStrings[i]))
    print("level: %d :: %s" % (i, myStrings[i]))