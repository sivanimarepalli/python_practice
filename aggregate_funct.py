# Implement python function aggregate(*nums, op="sum") supporting:
# op="sum" → sum of numbers,
# op="avg" → average (float),
# op="max" → maximum.
# If no numbers provided, return None.
def aggregate(*nums,op="sum"):
    s=0
    if len(nums)==0:
        return None
    else:
        if op=="sum":
            for ele in nums:
                s=s+ele
            return s
        elif op=="max":
            m=max(nums)
            return m
        elif op=="avg":
            s=sum(nums)
            a=s/len(nums)
            return a
res=aggregate(15,9,8,7,6,op="avg")
print(res)