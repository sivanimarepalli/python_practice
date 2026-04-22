# Create a custom exception InvalidEmailError and raise it if an email does not contain @.
class InvalidEmailException(Exception):
    pass
email=input("Enter the email: ")
try:
    if email.__contains__("@"):
        print("Valid")
    else:
        raise InvalidEmailException("Invalid Email Exception has occured")
except InvalidEmailException as inv:
    print(inv)