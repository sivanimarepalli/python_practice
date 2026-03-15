# Replace all digits in a string with #.
str1=input("Enter a string: ")
for ch in str1:
    if ch>="0" and ch<="9":
        str1=str1.replace(ch,"#")
print(str1)