
def mirrored_digits_length(n):
    # parameter n is a positive integer
    # your function should return the number of steps
    pass

def isPalindrome(n):

    myStr = str(n)
    revStr = myStr[::-1]

    if (myStr == revStr):
        return True
    else:
        return False

def findPalindrome(n, lvl):
    found = isPalindrome(n)
    if (found):
        #print("Found %d!!" % n)
        return n, lvl
    else:
        revStr = str(n)[::-1]
        m = n + int(revStr)
        #print("finding %s %d" % (revStr, m))
        return findPalindrome(m, lvl+1)

n = 87 
final, lvl = findPalindrome(n,0)
print("value: %d isPalindrome: %s" % (n, isPalindrome(n)))
print("value: %d findPalindrome: %d levels: %d" % (n, final, lvl))

n = 726
final, lvl = findPalindrome(n,0)

print("value: %d isPalindrome: %s" % (n, isPalindrome(n)))
print("value: %d findPalindrome: %d levels: %d" % (n, final, lvl))

n = 242
final, lvl = findPalindrome(n, 0)

print("value: %d isPalindrome: %s" % (n, isPalindrome(n)))
print("value: %d findPalindrome: %d levels: %d" % (n, final, lvl))
