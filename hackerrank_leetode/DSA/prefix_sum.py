# Given an array of integers, build a prefix sum array where each element at index i is the sum of all elements from 0 to i.
# Example:
# Input: [2, 4, 6, 8]
# Output: [2, 6, 12, 20]
nums=[2,4,6,8]
prefix_sum=0
prefix_list=[]
for ele in nums:
    prefix_sum+=ele
    prefix_list.append(prefix_sum)
print(prefix_list)