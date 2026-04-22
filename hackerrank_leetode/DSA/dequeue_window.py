# Given an array and a window size k, use a deque to find the maximum element in each sliding window.
from collections import deque
d=deque()
n=int(input("Enter the size of the deque"))
for _ in range(n):
    ele=int(input())
    d.append(ele)
k=int(input("Enter the window size: "))
max_elements=[]
max_ele=float('-inf')
for i in range(0,n-k+1):
    max_ele=float('-inf')
    for j in range(i,i+k):
        max_ele=max(d[j],max_ele)
    max_elements.append(max_ele)
print(max_elements)