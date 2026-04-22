# "Write a function to find the maximum product of a contiguous subarray in an array of integers (including negatives and zeros).
# Example:
# Input: [2, 3, -2, 4]
# Output: 6 (subarray [2, 3])"
# Brute-force->o(n^2)
def max_product(nums):
    max_pro=float('-inf')
    for i in range(len(nums)):
        prod=1
        for j in range(i,len(nums)):
            prod*=nums[j]
            max_pro=max(prod,max_pro)
    return max_pro
# optimized-> O(n)
def max_product_optimize(nums):
    curr_max=nums[0]
    curr_min=nums[0]
    global_max=nums[0]
    for i in nums[1:]:
        if i<0:
            curr_max,curr_min=curr_min,curr_max
        temp_max=curr_max
        curr_max=max(i,curr_min*i,curr_max*i)
        curr_min=min(i,temp_max*i,curr_min*i)
        global_max=max(global_max,curr_max)
    return global_max
nums=[2,3,-2,4]
res=max_product(nums)
print(res)
ans=max_product_optimize(nums)
print(ans)