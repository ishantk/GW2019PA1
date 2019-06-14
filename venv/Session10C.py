# Class and Object Relationship
class CA:

    num = 101

    def __init__(self):
        self.num = 102

    def show(self):
        print("num is:",self.num)
        print("num is:", CA.num)

cRef = CA()
cRef.show()

# Rule : Property of class can be accessed by class name
# or Ref Var of Object i.e. self
# But Property of Object is not accessible by Class

# Rule : If object has no attribute which is further available in class, object can access it !!
#        if object shall have it, object will use its own !! :)