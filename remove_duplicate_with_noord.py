# Convert a list with duplicates into a list of unique elements while preserving no order.
# logic-1
my_list=[]
n=int(input("Enter the size of the list: "))
for _ in range(n):
    my_list.append(int(input()))
res=[]
for ele in my_list:
    if ele not in res:
        res.append(ele)
print(res)

# logic-2
res2=set(my_list)
print("res2:",res2)