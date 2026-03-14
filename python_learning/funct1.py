def display_invoice(username,amount,due_date):
    print(f" Hello {username}")
    print(f"Your bill of ${amount:.2f} is due:{due_date}")


display_invoice("Sivani", 15000,"15-03-26") 

# return = it is a statement used to end a function and send a result back to the caller
# eg:-1
def add(x,y):
    z=x+y
    return z

print("THE SUM OF X AND Y IS: ",add(5,2))

# ex:-2
def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first+" "+last

full_name=create_name("sivani","marepalli")
print("THE FULL NAME IS: ",full_name)