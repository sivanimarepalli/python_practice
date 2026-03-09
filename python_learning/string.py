name=input("Enter your name: ")
print(len(name)) #counts the no.of characters in the given string and returns an int value as length'
print(name.find("i"))# prints the index of  first occurence of character provided
print(name.rfind("i"))# prints the index of last occurence of the character provided
print(name.capitalize())# returns a string by capitalizing the first letter
print(name.upper())# returns a string after converting all chars to uppercase letters
print(name.lower())# returns a string after converting all chars to lowercase letters
print(name.isdigit())# returns true if the string contains numbers else false
print(name.isalpha())# returns true if the string only contains alphabets else false
print(name.isalnum())# returns true if the string contains both alphabets and nums else false
print(name.count("i"))# returns the count of the character provided in the string
print(name.replace("i","iii"))# replaces the first character in the string with the second one
#print(help(str)) to learn more about strings
# indexing:
credit_num="1234-5678-9017-5684"
print(credit_num[0])
print(credit_num[2:9])
print(credit_num[2:9:2])
# reverse the credit_num value to cn
cn=credit_num[::-1]
print(cn)