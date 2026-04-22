# Write a recursive version of the binary search algorithm for a sorted array.
def binary_recur(nums,target,l,h):
   if l>h:
        return -1
   mid=(l+h)//2
   if nums[mid]==target:
        return mid
   elif nums[mid]<target:
        return binary_recur(nums,target,mid+1,h)
   else:
        return binary_recur(nums,target,l,mid-1)
    
nums=[2, 3, 4, 10, 40]
target=10
res=binary_recur(nums,target,0,len(nums)-1)
print(res)