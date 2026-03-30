# solving fibonacci using dp.
def getAutoSaveInterval(n):
    # Write your code here
    dp=[0]*(n+1)
    if n==0:
        return 1
    elif n==1:
        return 2
    dp[0],dp[1]=1,2
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]