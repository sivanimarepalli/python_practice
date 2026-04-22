# Given a sorted array and a target, return the starting and ending position of the target using binary search.
def first_binary_search(nums,target):
    l=0;h=len(nums)-1
    mid=0
    ans=-1
    while l<=h:
        mid=(l+h)//2
        if nums[mid]==target:
            h=mid-1
            ans=mid
        elif nums[mid]<target:
            l=mid+1
        else:
            h=mid-1
    return ans
def last_binary_search(nums,target):
    l=0;h=len(nums)-1
    mid=0
    ans=-1
    while l<=h:
        mid=(l+h)//2
        if nums[mid]==target:
            l=mid+1
            ans=mid
        elif nums[mid]<target:
            l=mid+1
        else:
            h=mid-1
    return ans
nums=[1, 2, 2, 2, 3, 4]
target=2
i=first_binary_search(nums,target)
j=last_binary_search(nums,target)
print(i,j)