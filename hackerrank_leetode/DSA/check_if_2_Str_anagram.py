# Check if two strings are anagrams by comparing their character frequency maps.
s1=input("Enter a string: ")
s2=input("Enter another string: ")
freq1=dict()
freq2=dict()
for ele in s1:
    if ele in freq1:
        freq1[ele]+=1
    else:
        freq1[ele]=1
for e in s2:
    if e in freq2:
        freq2[e]+=1
    else:
        freq2[e]=1
print(freq1==freq2)
        
