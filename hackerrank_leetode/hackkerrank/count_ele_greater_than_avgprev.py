# Question: Given an array of positive integers, return the number of elements that are strictly greater than the average of all previous elements. Skip the first element.

# bruteforce -O(N*N):
def countResponseTimeRegressions(responseTimes):
    # Write your code here
    avg=0
    s=0
    cnt=0
    for i in range(len(responseTimes)):
        s=0
        avg=0
        if i==0:
            continue
        else:
            for num in range(0,i):
                s+=responseTimes[num]
            avg=s/i
            if responseTimes[i]>avg:
                cnt+=1            
    return cnt
# optimized- O(N):
def countResponseTimeRegressions(responseTimes):
    # Write your code here
    avg=0
    s=0
    cnt=0
    for i in range(len(responseTimes)):
        avg=0
        if i==0:
            s+=responseTimes[i]
            continue
        else:
            avg=s/i
            if responseTimes[i]>avg:
                cnt+=1  
            s+=responseTimes[i]          
    return cnt