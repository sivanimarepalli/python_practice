# Given a string of brackets like "({[]})", use a list as a stack to determine if the string is balanced.
def is_balanced(s):
    stack=[]
    for ch in s:
        if ch=='(' or ch=='{' or ch=='[':
            stack.append(ch)
        elif not stack:
            return False
        else:
            top=stack[-1]
            if top=='{' and ch=='}' or top=='(' and ch==')' or top=='[' and ch==']':
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
    else:
        return False
        

str1=input("Enter the string of brackets: ")
if is_balanced(str1):
    print("Balanced")
else:
    print("Not Balanced")

        