import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    # iterate top to bottom & left to right across a tree
    # iterative function, not recursive, see below.
    def levelOrder(self,root):
        #Write your code here
        q = list()
        q.insert(0,root)    

        while (q):
            subTree = q.pop()
            sys.stdout.write("%s " % subTree.data)
            if (subTree.left<>None):
                q.insert(0,subTree.left)
            if (subTree.right<>None):
                q.insert(0,subTree.right)





T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)