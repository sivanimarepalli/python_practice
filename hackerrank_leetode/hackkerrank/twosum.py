# return the indices of values that sum to target if not return [-1,-1]
# approach- use hashmap
def findTaskPairForSlot(taskDurations, slotLength):
    # Write your code here
    res={}
    for i,num in enumerate(taskDurations):
        c=slotLength-num
        if c in res:
            return[res[c],i]
        res[num]=i
    return [-1,-1]