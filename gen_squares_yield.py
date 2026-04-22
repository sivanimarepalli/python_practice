# Write two generators:
# gen_numbers() yields numbers 1–10.
# gen_squares() takes numbers and yields their squares.
# Chain them together to print squares of 1–10.
def gen_numbers():
    for i in range(1,11):
        yield i
def gen_squares(numbers):
    for i in numbers:
        sqr=i*i
        yield sqr
res=gen_squares(gen_numbers())
for i in res:
    print(i)