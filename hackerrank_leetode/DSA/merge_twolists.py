# Given two sorted linked lists, merge them into a single sorted list.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node
l1=LinkedList()
l1.insert_begin(10)
l1.insert_end(20)
l1.insert_end(30)
l1.insert_end(40)
l1.insert_end(60)
l2=LinkedList()
l2.insert_begin(-2)
l2.insert_end(-1)
l2.insert_end(2)
l2.insert_end(6)
l2.insert_end(7)
p1=l1.head
p2=l2.head
while p1 and p2:
    if p1.data<p2.data:
        print(p1.data)
        p1=p1.next
    else:
        print(p2.data)
        p2=p2.next
while p1:
    print(p1.data)
    p1=p1.next
while p2:
    print(p2.data)
    p2=p2.next
