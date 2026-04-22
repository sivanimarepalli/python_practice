# Given a string, compress it by replacing consecutive repeating characters with the character followed by its count (e.g., "aaabb" → "a3b2")
s=input("Enter a string: ")
cnt=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        cnt+=1
    else:
        print(s[i-1]+str(cnt),end="")
        cnt=1
print(s[-1]+str(cnt),end="")


