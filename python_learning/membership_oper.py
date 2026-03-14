word="Apple"
letter=input("Guess a letter in the secret word: ")
if letter in word:
    print(f"There is a {letter} in the word")
else:
    print(f"{letter} not found")

# example-2:
students={"spongebob","patrick","sizuka"}
student =input("Enter the name of the student: ")
if student not in students:
    print(f"{student} name is not available.")
else:
    print(f"{student} name is available")

# example-3:
grades={"sizuka":99,"doremon":55,"spongebob":79}
studentt=input("ENter the name of the student: ")
if studentt in grades.keys():
    print(f"{studentt} got {grades.get(studentt)} marks")
else:
    print(f"{studentt} not found")

# example-4:
email="abccc@gmail.com"
if "@" and "." in email:
    print(f"{email} is an valid email")
else:
    print({f"{email} is not a valid one."}) 