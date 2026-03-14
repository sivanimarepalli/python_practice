# a person can climb stairs either by climbing 1 or 2 stairs at a time. identify the no.of ways a person can climb
# solution in recursion (But TLE)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)
obj=Solution()
n=int(input("Enter a n value to check: "))
result= obj.climbStairs(n)
print(result)
        