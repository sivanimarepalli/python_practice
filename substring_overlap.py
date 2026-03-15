# Count occurrences of a substring allowing overlaps.
str1=input("Enter a string to check overlapping substrings: ")
substring=input("Enter a substring that needs to be checked: ")
c=0
l=len(substring)
for ch in range(len(str1)-l+1):
    if str1[ch:ch+l]==substring:
        c+=1    
print(c)

