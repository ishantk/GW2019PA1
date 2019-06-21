"""
    @staticmethod
    @classmethod

    lambdas

    map filter reduce

    generators

    nested functions

    functions as inputs and returns

    DialogFlow Intro
"""

class Point:

    # self is Reference to Current Object
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    """    
    def __init__(self, data):
        points = data.split(",")
        self.x = int(points[0])
        self.y = int(points[1])
    """
    # If you wish to have more different ways other than __init__
    # We can create methods of our own choice
    # cls is Reference to Class
    @classmethod
    def createPoint(cls, data):
        points = data.split(",")
        # cls(int(points[0]), int(points[1])) -> Creates a new Object using __init__(self, x, y)
        refToObj = cls(int(points[0]), int(points[1]))
        return refToObj

    @classmethod
    def createPointFromFirebase(cls,someOtherInput):
        pass

    def showPoint(self):
        print("Point is:",self.x, self.y)

    @staticmethod
    def greet(name):
        print("Hello,",name)

    @staticmethod
    def check(i1, i2):
        return i1>i2

p1 = Point()
p2 = Point(10, 20)

p1.showPoint()
p2.showPoint()

file = open("points.txt", "r")
data = file.readline()
print(data)

# points = data.split(",")
# print(points[0], points[1])
# print(type(points[0]), type(points[1]))
#
# p3 = Point(int(points[0]), int(points[1]))
# p3.showPoint()

p3 = Point.createPoint(data)
p3.showPoint()

print("Is X in p3 Greater than Y: ", Point.check(p3.x, p3.y))

Point.greet("John")