# Question: Given a string, check if all brackets ('()', '{}', '[]') are properly matched and nested. Return 1 if valid, otherwise return 0.
def areBracketsProperlyMatched(code_snippet):
    # Write your code here
    stack=[]
    for ch in code_snippet:
        if ch=='(' or ch=='{' or ch=='[':
            stack.append(ch)
        elif ch=='}' or ch==']' or ch==')':
            if stack:
                top=stack[-1]
            else:
                return 0                
            if top == '{' and ch=='}' or top == '[' and ch==']' or top == '(' and ch==')':
                stack.pop()
            else:
                return 0
    if len(stack)==0:
        return 1
    else:
        return 0