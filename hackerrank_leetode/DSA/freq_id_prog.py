# Given a list of product IDs, use frequency counting to find which IDs appear more than once.
l1=list(input("Enter the list of id's").split())
freq=dict()
for ele in l1:
    if ele in freq:
        freq[ele]+=1
    else:
        freq[ele]=1
for key,val in freq.items():
    if val>1:
        print(key,val)   