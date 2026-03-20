# Count the frequency of each word in a given paragraph and return a dictionary sorted by frequency.
paragraph=input("Enter the paragraph: ")
words=paragraph.split()
my_dict={}
n=len(words)
for i in range(n):
    key=words.count(words[i])
    value=words[i]
    my_dict[key]=value

my_dict=sorted(my_dict)
for key,val in my_dict.items():
    print(key,val)