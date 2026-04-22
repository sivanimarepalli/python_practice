#  Return list of (element, count) in order of first appearance.
list1=[]
n=int(input("Enter the size of list: "))
for _ in range(n):
    ele=int(input())
    list1.append(ele)

list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)

res=[]
for e in list2:
    occ_cnt=(e,list1.count(e))
    res.append(occ_cnt)

print(res)