# Given a list of strings, sort them by their length using any efficient sorting technique.
l1=list(input("Enter strings separated by space: ").split())
sorted_list=sorted(l1,key= lambda x:len(x))
for wrd in sorted_list:
    print(wrd,end=" ")