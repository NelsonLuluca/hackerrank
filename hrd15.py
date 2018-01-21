class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next  

    def getTail(self,head):
        current = head
        if current.next:
            while current.next:
                current = current.next
        return current

    def insert(self,head,data): 
    #Complete this method
        if head:
            tail = head
            if tail.next:
                while tail.next:
                    tail = tail.next
            temp = Node(data)
            tail.next = temp
            return head
        else:
            temp = Node(data)
            return temp

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);
