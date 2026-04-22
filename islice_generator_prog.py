# Use itertools.islice() to take the first 5 elements from an infinite generator of multiples of 3.
from itertools import islice,count
for i in islice(count(0,3),5):
    print(i)