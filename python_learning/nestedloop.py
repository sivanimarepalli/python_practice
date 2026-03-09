for y in range(3):
    for x in range(1,10):
        print(x,end="")
    print()

# create a rectangle by taking input from the user
rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns:  "))
symbol=input("Enter a symbol to use: ")
for i in range(rows):
    for j in range(cols):
        print(symbol,end=" ")
    print()