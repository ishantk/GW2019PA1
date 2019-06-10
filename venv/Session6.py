# Functions - f(x) = x*x
#             f(2) = 2*2 = 4
# Methods/ Procedures/ Routines
"""
    Function
    1. Name
    2. Inputs(May or May Not) | Parameters | Arguments
    3. return(May or may Not) | Acknowledgement
    4. Definition(May or May Not) -> Sequence

    Why Loops ?
        Where we write statements
        which are repeated again and again

    Why Functions ?
        Group of statements / logic which has to
        be executed again and again

    Modularization is something which we are doing
    in our program to simplify the process
"""

# Definition of function : addNumbers
# num1 and num2 are inputs
def addNumbers(num1, num2):
    num3 = num1 + num2
    #print("Sum of {} and {} is {}".format(num1, num2, num3))
    return num3

# result = addNumbers(10, 20) # Execution of addNumbers function
# print("Sum is:",result)
# print(addNumbers(20, 33))
# print("Sum is:",addNumbers(45, 78))
print(addNumbers(-12, 76))

