# Rotate List Right by K (No Slicing). Rotate a list to the right by K positions. Do not use slicing.
#TC: o(n)+o(n)=>o(n)
# nums=[1,2,3,4,5]
# k=2
# n=len(nums)
# d=k%n
# for i in range(n-k,n):
#     print(nums[i],end=" ")
# for j in range(0,n-k):
#     print(nums[j],end=" ")

# TC: o(n): (optimized)
nums=[1,2,3,4,5]
k=2
n=len(nums)
d=k%n # rotating n elements k times is similar to k%n
def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    return nums

reverse(nums,0,n-1) # rotate entire list
reverse(nums,0,d-1) # rotate till d from start
reverse(nums,d,n-1) # rotate from d till the end
print(nums)
