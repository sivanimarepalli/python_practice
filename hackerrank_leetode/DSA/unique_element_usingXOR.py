# In an array where every element appears twice except one, find the unique element using bitwise XOR.
# Example:
# Input: [2, 3, 2, 4, 4] → Output: 3.
nums=[2,3,2,4,4]
res=nums[0]
for ele in range(1,len(nums)):
    res=res^nums[ele]
print(res)
