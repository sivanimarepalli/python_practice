def fibbon(n):
    if n<=1:
        return n
    else:
        return fibbon(n-1)+fibbon(n-2)
num=int(input("Enter the number: "))
print(fibbon(num))
