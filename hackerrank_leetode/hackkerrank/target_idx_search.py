# Question: Given a sorted array of distinct integers and a target value, return the index of the target or -1 if not found.
# approach:linear search: TC-> O(N)
def binarySearch(nums, target):
    # Write your code here
    res=-1
    for i in range(len(nums)):
        if nums[i]==target:
            res=i
    return res
# Binary Search TC: O(logN)

def binarySearch(nums, target):
    # Write your code here
    l=0
    h=len(nums)-1
    m=0
    while l<=h:
        m=(l+h)//2
        if nums[m]==target:
            return m
        elif nums[m]>target:
            h=m-1
        elif nums[m]<target:
            l=m+1
    return -1