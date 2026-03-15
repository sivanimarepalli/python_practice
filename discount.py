# Receive an amount, apply discount: <1000 → 0%, 1000–4999 → 5%, >=5000 → 10%. Return final payable.
amount=float(input("enter the price: "))
discount=0.0
if amount<1000:
    print(amount)
elif amount>=1000 and amount<=4999:
    discount=amount*(5/100)
    print(f"The amount needs to be paid after discount is: {amount-discount}")
elif amount>=5000:
    discount=amount*(10/100)
    print(f"The amount needs to be paid after discount is: {amount-discount}")