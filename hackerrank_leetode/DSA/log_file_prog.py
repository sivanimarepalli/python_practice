# Given a log file with event types (e.g., INFO, WARN, ERROR), count the frequency of each event type and identify the most common one.
s=input("Enter the event types: ")
l1=list(s.split())
print(l1)
d=dict()
for i in range(0,len(l1)):
    if l1[i] in d:
        d[l1[i]]+=1
    else:
        d[l1[i]]=1
m=0
event=""
for key,val in d.items():
    if val>m:
        m=val
        event=key
print(event,m)