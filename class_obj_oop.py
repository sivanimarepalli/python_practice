# Create a class Student with a class variable school_name and instance variables name and roll_no.
# Show how changing school_name affects all objects.
class Student:
    school_name="subbammadevi school"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

s1=Student("sivani",6)
print(s1.name)
print(s1.roll_no)
Student.school_name="Abhyasa"
print(s1.school_name)
s2=Student("bharathi",15)
print(s2.name)
print(s2.roll_no)
print(s2.school_name)