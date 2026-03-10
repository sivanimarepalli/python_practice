# search insert position -> leetcode
# if you find the target value in the given array return it's index. else return the index it should be inserted.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       l=0
       h=len(nums)-1
       m=0
       while l<=h:
        m=(l+h)//2
        if nums[m]==target:
            return m
        elif nums[m]>target:
          h=m-1
        else:
            l=m+1
       return l
nums=[1,3,5,6]
target=5
obj1=Solution()
result=obj1.searchInsert(nums,target)
print(result)