# Variable Arguments
def addNumbers(*args):
    print(args)
    print(type(args))

    sum = 0
    for n in args:
        sum = sum + n

    print("sum is:",sum)

addNumbers(10, 20, 30, 40, 50)

"""
def addNumbers(tpl):
    print(tpl)
    print(type(tpl))

addNumbers((10, 20, 30))
"""