# From a list, find the index of the second largest distinct element. If it does not exist, return -1.
nums=[4, 8, 6, 8, 5]
max_ele=max(nums)
res=-1
for i in range(len(nums)):
        if nums[i]==max_ele:
              continue
        else:
               res=max(res,nums[i])

if res!=-1:
       print(nums.index(res))
else:
       print(res)