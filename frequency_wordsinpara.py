# Count the frequency of each word in a given paragraph and return a dictionary sorted by frequency.
paragraph=input("Enter the paragraph: ")
words=paragraph.split()
sorted_words=sorted(words)
print(sorted_words)
my_dict={}
n=len(words)
for i in range(n):
    if sorted_words[i] not in my_dict:
        key=sorted_words.count(sorted_words[i])
        value=sorted_words[i]
        my_dict[value]=key
for key,val in my_dict.items():
    print(key,val)