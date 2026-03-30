# Given n slots numbered 0 to n-1, return the number of ways to fill all slots where each operation covers either 1 slot or 2 adjacent slots.
# pattern similar to climbing stairs.
def countInstallationSequences(n):
    # Write your code here
    dp=[0]*(n+1)
    if n==0:
        return 1
    if n==1 or n==2:
        return n
    dp[0]=1
    dp[1],dp[2]=1,2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]