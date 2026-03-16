# From a list, remove duplicates while keeping the last occurrence of each element.
nums=[1, 2, 3, 2, 4, 1]
new_num=[]
for i in reversed(nums):
    if i not in new_num:
        new_num.append(i)
    else:
        continue
for j in reversed(new_num):
    print(j,end=" ")