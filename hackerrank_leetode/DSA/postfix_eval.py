#Given tokens of an RPN expression (e.g., ["2","1","+","3","*"]), use a list as a stack to compute the result.
def oper(e,a,b):
   if e=="+":
      return a+b
   elif e=="-":
      return a-b
   elif e=="*":
      return a*b
   elif e=="/":
      return a//b
my_list=[]
n=int(input("Enter the size of list: "))
for _ in range(n):
    ele=input()
    my_list.append(ele)
stack=[]
for e in my_list:
   if e.isdigit():
      stack.append(e)
   elif e=="+" or e=="-" or e== "*" or e=="/":
      top1=int(stack.pop())
      top2=int(stack.pop())
      res=oper(e,top2,top1)
      stack.append(int(res))
if len(stack)==1:
   print(stack[0])