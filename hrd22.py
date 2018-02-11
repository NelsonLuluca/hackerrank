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

    def getHeight(self,root):
        #Write your code here
        bestHeight = 0
        rightHeight = 0
        leftHeight = 0
        if (root.left<>None):
            #print("following left with %s" % root.left.data)
            leftHeight = self.getHeight(root.left) + 1
        if (root.right<>None):
            #print("following right with %s" % root.right.data)
            rightHeight = self.getHeight(root.right) + 1

        if rightHeight > leftHeight:
            bestHeight = rightHeight
        else:
            bestHeight = leftHeight

        return bestHeight


T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print height       