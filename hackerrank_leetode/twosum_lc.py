# question: identify the indices of the list and return them if the sum is target and those indices are not same

# brute-force solution tc: o(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l1=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]) == target:
                    l1.append(i)
                    l1.append(j)
        return l1

obj=Solution()
l=[2,7,11,15]
target =9
result=obj.twoSum(l,target)
print(result)