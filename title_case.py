# Convert a sentence to title case but keep known abbreviations (e.g., AI, ML) uppercase.
str1=input("Enter a sentence: ")
l1=str1.split(" ")
abbrevations=["AI","ML","BSNL","NASA","ISRO","CPU","GPU"]
for ele in range(len(l1)):
    if l1[ele].upper() in abbrevations:
        l1[ele]=l1[ele].upper()
    else:
        l1[ele]=l1[ele].title()
        
print(" ".join(l1))
