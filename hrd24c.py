class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
        p = Node(data)        
        if head==None:
            head=p
        elif head.next==None:
            head.next=p
        else:
            start=head
            while(start.next!=None):
                 start=start.next
            start.next=p
        return head 
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next  

    def removeDuplicates(self,head):
        #Write your code here

        curr=None
        prev = head
        myCollection = []
        # head might be null so check first
        if (prev):
            myCollection.append(prev.data)
            curr = head.next
        # iterate through the linked list
        while (curr):
            #print("WHILE list contents")
            #self.display(head)
            #print("\n")
            # found a duplicate in my collection
            if curr.data in myCollection:
                prev.next = curr.next
            else:
                myCollection.append(curr.data)
            prev = curr
            curr = curr.next

        #print("SeanList")
        #self.display(head)
        return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)   
head=mylist.removeDuplicates(head)
mylist.display(head);





