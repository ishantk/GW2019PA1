"""
    Student
        name
        phone
        email
        password
        isCollegeTraining
        collegeName
        rollNum

"""

"""
class Student:
    pass

s1 = Student()
s2 = Student()

s1.name = "John"
s1.phone = "+91 99999 77777"
s1.email = "john@example.cm"
s1.password = "pass123"
s1.isCollegeTraining = True
s1.collegeName = "ABC International"
s1.rollNum = 22

s2.fullName = "Fionna"
s2.phn = "+91 8888 77777"
s2.email = "fionna@example.cm"
s2.passphrase = "pass123"
s2.isCollegeTraining = True
s2.collegeName = "ABC International"
s2.rollnum = 24

students = [s1, s2]

print(s1.__dict__)
print(s2.__dict__)

# Challenge : No Standardization
# Solution  : Constructors
"""

class Student:

    schoolName = "ATPL"

    # self is a reference variable which will hold hashcode of current object
    # __init__ is known as constructor
    # Constructor is property of class
    def __init__(self, name, phoneNumber, email, password, isCollegeTraining, collegeName, rollNum):
        print(">> self is:",self)
        self.fullName = name
        self.phone = phoneNumber
        self.email = email
        self.password = password
        self.isCollegeTraining = isCollegeTraining
        self.collegeName = collegeName
        self.rollNum = rollNum

    # Over-Writing -> A new constructor will be created and old will be removed
    # def __init__(self, name, phone):
    #     self.name = name
    #     self.phone = phone

    # showStudentDetails function is property of class
    def showStudentDetails(self):
        print("======================")
        print("Details of",self.fullName)
        print("Phone:\t",self.phone)
        print("Roll:\t", self.rollNum)
        print("======================")

s1 = Student("John", "+91 99999 77777", "john@example.com", "pass123", True, "ABC International", 22)    # Student.__init__(s1,)
print("s1 is:",s1)


s2 = Student("Fionna", "+91 888888 77777", "fionna@example.com", "pass123", True, "ABC International", 33)    # Student.__init__(s1,)
print("s2 is:",s2)

s1.age = 22
s1.vehicleNum = "PB10AB1234"

s1.fullName = "John Watson"
s2.fullName = "Fionna Flynn"

# del s1.age
# del s1.phone

# print(s1.__dict__)
# print(s2.__dict__)

# s1.showStudentDetails() # Student.showStudentDetails(s1)
# s2.showStudentDetails()

Student.showStudentDetails(s1)
Student.showStudentDetails(s2)

print()

print(s1.__dict__)
print(Student.__dict__)
