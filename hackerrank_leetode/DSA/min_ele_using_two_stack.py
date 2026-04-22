# Implement a stack that returns the minimum element in O(1) time.
class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            raise Exception ("stack is empty")
        return self.items.pop()
    def is_empty(self):
        return len(self.items)==0
    def get_min(self):
        return min_stack.top()
    def top(self):
        return self.items[-1]

actual_stack=Stack()
min_stack=Stack()
n=int(input("Enter the no.of vals to be inserted: "))
while n>0:
 val=int(input())
 actual_stack.push(val)
 if min_stack.is_empty() or val<=min_stack.top():
     min_stack.push(val)
 n-=1
actual_stack_poppedval=actual_stack.pop()
if actual_stack_poppedval == min_stack.top():
    min_stack.pop()
if not min_stack.is_empty():
    print(f"min value is : {min_stack.top()}")
else:
    print("Stack is empty")
