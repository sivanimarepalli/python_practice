# Use a generator expression to compute the sum of squares of numbers from 1 to 100.
res=(i*i for i in range(1,99))
print(sum(res))