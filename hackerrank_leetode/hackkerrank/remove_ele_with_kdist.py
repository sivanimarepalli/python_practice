# Question: Given a non-decreasing array of integers and an integer K, remove in-place any element that is within K of the previous kept element and return the new length. Use constant extra space and single pass with two pointers.
def debounceTimestamps(timestamps, K):
    # Write your code here
    if  not timestamps:
        return 0
    last_kept=timestamps[0]
    
    cnt=1
    for i in range(1,len(timestamps)):
        if (timestamps[i]-last_kept)>=K:
            cnt+=1
            last_kept=timestamps[i]
        else:
            continue
    return cnt