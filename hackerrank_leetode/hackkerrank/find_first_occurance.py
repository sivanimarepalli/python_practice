# Question: Given a sorted array of integers that may contain duplicates, return the index of the first occurrence of a target value or -1 if not found.
# Time complexity: o(N): "note: Optimized code for unsorted array"
def findFirstOccurrence(nums, target):
    # Write your code here
    res=-1
    for i in range(len(nums)):
        if nums[i]==target:
            res=i
            break
    return res
# Using binary Search Tc:o(logn) "note: only for sorted array"
