# Running Maximum with Reset Track the running maximum in a list. If a value is ≤ 0, reset the running maximum to 0. Output a list containing the running maximum values at each step.
nums=[3, 5, -1, 4, 6, 0, 2]
res=[]
max_ele=0
for i in range(len(nums)):
    max_ele=max(max_ele,nums[i])
    
    res.append(max_ele)
print(res)
