# a person can climb stairs either by climbing 1 or 2 stairs at a time. identify the no.of ways a person can climb
# solution in recursion (But TLE)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)

# solution using dynamic programming
class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        if n==1 or n==2:
            return n
        dp[0],dp[1]=1,1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
        

obj=Solution()
n=int(input("Enter a n value to check: "))
result= obj.climbStairs(n)
print(result)
        