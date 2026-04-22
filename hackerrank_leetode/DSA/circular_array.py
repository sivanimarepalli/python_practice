# For a circular array A (the element after the last is the first), compute the Next Greater Element for each index using a stack.
arr=[]
n=int(input("enter the size of the list: "))
for _ in range(n):
    ele=int(input())
    arr.append(ele)
res=[]

for i in range(n):
    found=False
    for step in range(1,n):
        j=(i+step)%n
        if arr[j]>arr[i]:
            res.append(arr[j])
            found=True
            break
    if not found:
        res.append(-1)
print(res)
