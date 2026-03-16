try:
    num=int(input("Enter a number: "))
    print(1/num)
except ZeroDivisionError:
    print("You can't divide by 0.")
except ValueError:
    print("Enter only numbers please")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some clean up here")