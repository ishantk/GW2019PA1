# Any .py file is called as Python Module

companyName = "ABC International"

def hello(name):
    print("Hello,",name)

def bye(name):
    print("Bye,",name)

class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def showEmployee(self):
        print("{} | {} | {}".format(self.id, self.name, self.salary))