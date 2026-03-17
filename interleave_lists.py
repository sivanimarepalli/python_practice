# Combine two lists element-wise. Stop when the shorter list ends.
list1=[1,5,6,8,9]
list2=[-1,6,-2]
res=[]
n1=len(list1)
n2=len(list2)
res_n=0
if n1<n2: 
    res_n=n1
else: 
    res_n=n2
for i in range(res_n):
    res.append(list1[i])
    res.append(list2[i])
res.sort()
print(res)