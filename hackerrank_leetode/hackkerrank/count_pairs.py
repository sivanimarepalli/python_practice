# Given a sorted array of positive integers and a target value, count the number of pairs (i, j) where i < j and array[i] + array[j] <= target.
# bruteforce code: O(N^2):
def countAffordablePairs(prices, budget):
    # Write your code here
    cnt=0
    for i in range(len(prices)):
        for j in range(1,len(prices)):
            if i<j and prices[i]+prices[j]<=budget:
                cnt+=1
    return cnt
# optimized code: O(N)
def countAffordablePairs(prices, budget):
    # Write your code here
    cnt=0
    l=0
    h=len(prices)-1
    while l<h:
        if (prices[l]+prices[h])<=budget:
            cnt+=h-l
            l+=1
        else:
            h-=1
    return cnt