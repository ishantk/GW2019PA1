# Default Argument Values in Functions
def addNumbers(num1, num2, num3=0):
    sum = num1 + num2 + num3
    print("Sum is:",sum)

print("addNumbers is:",addNumbers)

# Update Operation on Functions
def addNumbers(num1, num2, num3=0, num4=0):
    sum = num1 + num2 + num3 + num4
    print("Sum is:",sum)

print("addNumbers is:",addNumbers)

addNumbers(10, 20)
addNumbers(10, 20, 30)