'''
Sample Input

6
1
2
2
3
3
4

Sample Output

1 2 3 4 
'''


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
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        current = head
        next_next = None
        if current == None:
            return head
        while current.next != None:
            if current.data == current.next.data:
                next_next = current.next.next
                current.next = next_next
            else:
                current = current.next
        return head
        #Write your code here

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 