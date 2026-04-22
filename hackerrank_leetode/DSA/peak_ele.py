# Find a peak element in an array (an element that is greater than its neighbors) using binary search in O(log n) time.
def bin_search(nums):
    l=0;h=len(nums)-1
    mid=0
    while l<h:
        mid=(l+h)//2
        if nums[mid]<nums[mid+1]:
            l=mid+1
        else:
            h=mid
    return l
nums=[1, 2, 2, 2, 3, 4]
cnt=bin_search(nums)
print(nums[cnt])
