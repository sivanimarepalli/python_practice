# Given an array containing only 0, 1, and 2, sort it without using any built-in sort function. 
nums=[]
n=int(input("Enter the size of the list: "))
for _ in range(n):
    ele=int(input())
    nums.append(ele)
cnt_z=0
cnt_o=0
cnt_t=0
for i in nums:
    if i==0:
        cnt_z+=1
    elif i==1:
        cnt_o+=1
    else:
        cnt_t+=1
res=[]
for _ in range(cnt_z):
    res.append(0)
for _ in range(cnt_o):
    res.append(1)
for _ in range(cnt_t):
    res.append(2)
print(res)