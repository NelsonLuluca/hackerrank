
import sys
from collections import deque

class Solution:
    sq = deque('')
    dq = deque('')

    # Write your code here
    def pushCharacter(self,c):
        self.sq.appendleft(c)
    def enqueueCharacter(self,c):
        self.dq.extend(c)
    def popCharacter(self):
        return self.sq.popleft()
    def dequeueCharacter(self):
        return self.dq.popleft()


# read the string s
s=raw_input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 

print("Stack: ")
print obj.sq
print("Queue: ")
print obj.dq


for i in range(l / 2):
    pc=obj.popCharacter()
    dc=obj.dequeueCharacter()
    if pc!=dc:
        print("NO STACK: %s QUEUE %s" % (pc,dc))
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    sys.stdout.write ("The word, "+s+", is a palindrome.")
else:
    sys.stdout.write ("The word, "+s+", is not a palindrome.")    
    
        