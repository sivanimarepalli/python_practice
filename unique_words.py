#Given text, return sorted unique words ignoring case.
text=input("Enter the text: ").lower() 
words=text.split()
my_set=set(words)
my_set=sorted(my_set)
print(my_set)