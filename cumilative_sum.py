# Compute the cumulative sum of elements in a list. Stop immediately when a negative number appears.
nums=[]
n=int(input("Enter the number of elements to insert: "))
for _ in range(n):
    e=int(input())
    nums.append(e)
total=0
for ele in nums:
    if ele<0:
        break
    total+=ele

print(f"Total cumilative sum is: {total}")