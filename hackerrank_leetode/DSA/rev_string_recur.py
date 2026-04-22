# Design a recursive function to reverse a string without using loops.
def rev_string(s):
    n=len(s)-1
    if n == 0:
        return s[0]
    return s[n]+rev_string(s[:n])
s=input("Enter a string: ")
res=rev_string(s)
print(res)