class Parent:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print(">> Parent Constructor Executed")

    def showDetails(self):
        print(">> Hello, ",self.fname, self.lname)

class Child(Parent): # Relationship -> IS-A
    pass

print("Parent Class Dictionary: ",Parent.__dict__)
print("Child Class Dictionary: ",Child.__dict__)


ch = Child("John", "Watson")
print(ch.__dict__)
ch.showDetails()

# Rule 1 : Whatsoever is in Parent is accessible to Child if not available in Child