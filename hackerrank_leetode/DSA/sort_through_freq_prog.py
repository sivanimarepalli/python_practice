# Given an array of integers, sort the elements by their frequency in descending order.
l1=list(input("Enter the integers separated by space: ").split())
freq=dict()
for ele in l1:
    if ele in freq:
        freq[ele]+=1
    else:
        freq[ele]=1
for key,val in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    for i in range(val):
        print(key,end=" ")