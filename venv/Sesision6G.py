# Passing Value
def squareOfNum(num):
    num = num * num
    print("square is {}".format(num))

n = 11
# squareOfNum(num=n)
squareOfNum(n)
print("n is:",n)

# modifying num will not change n


def addNumbers(a, b, c):
    d = a+b+c
    print(d)

addNumbers(10, 30, 20)
addNumbers(a=10, c=30, b=20)