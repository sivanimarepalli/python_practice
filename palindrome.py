str=input("Enter a string to check if it's palindrome or not: ")
str1=str[::-1]
if str==str1:
    print(f"{str} Palindrome")
else:
    print(f"{str}Not a palindrome")
#2.method-2
strng ="".join(reversed(str))
if str==strng:
    print("TRUE")
else:
    print("False")