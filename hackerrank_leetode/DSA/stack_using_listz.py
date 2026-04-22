stack=[]
n=int(input("Enter the size of stack: "))
for _ in range(n):
    ele=int(input())
    stack.append(ele)
print(f"The elements in the stack is: {stack}")
top_ele=stack.pop()
print(f" The top most element that got deleted is: {top_ele}")
print(f"The elements in stack after deletion in top ele is: {stack}")