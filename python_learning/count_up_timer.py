import time
def count(end,start=0): # default arguments should always be after normal arguments
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!!")

count(10)