# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def checkPrime(n):
    sq = math.sqrt(n)
    if n < 2:
        print ("Not prime")
        return
    elif n == 2:
        print("Prime")
        return
    for i in range(2, int(sq)+1):
        # as soon as we find a divisor we're not prime
        # so print status & shortcircuit out
        if n % i == 0:
            print("Not prime")
            return
    print("Prime")

rows=int(input())
for i in range(rows):
    n=int(input())
    #print("Checking... n=%d" % n)
    checkPrime(n)


