# is vs == Please Explore :)

# Why Inheritance ?
# Generalization leading to Customization
# In Programing Save my Time i.e. eliminate Redundant Code -> Code Reusability

# Inheritance : IS-A Relationship | Generalization
# Maruti Suzuki Swift Dzire IS-A Swift
# Amazon eCommerce example
# Shoe, Mobile , LEDTv etc....

"""
class Shoe:

    def __init__(self, pid, name, price, brand, color, size):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.color = color
        self.size = size

    def updateShoeDetails(self, pid, name, price, brand, color, size):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.color = color
        self.size = size

    def showShoeDetails(self):
        print("======Shoe Details=====")
        print(self.pid)
        print(self.name)
        print(self.price)
        print(self.brand)
        print(self.color)
        print(self.size)
        print("=======================")

class Mobile:

    def __init__(self, pid, name, price, brand, ram, memory):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.ram = ram
        self.memory = memory

    def updateMobileDetails(self, pid, name, price, brand, ram, memory):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.ram = ram
        self.memory = memory

    def showMobileDetails(self):
        print("======Mobile Details=====")
        print(self.pid)
        print(self.name)
        print(self.price)
        print(self.brand)
        print(self.ram)
        print(self.memory)
        print("=======================")

class LEDTv:

    def __init__(self, pid, name, price, brand, technology, screenSize):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.technology = technology
        self.screenSize = screenSize

    def updateLEDTvDetails(self, pid, name, price, brand, technology, screenSize):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.technology = technology
        self.screenSize = screenSize

    def showLEDTvDetails(self):
        print("======LEDTv Details=====")
        print(self.pid)
        print(self.name)
        print(self.price)
        print(self.brand)
        print(self.technology)
        print(self.screenSize)
        print("=======================")


sRef = Shoe(101, "AlphaBounce", 8000, "Adidas", "Black", 9)
mRef = Mobile(201, "iPhoneX", 60000, "Apple", 4, 128)
lRef = LEDTv(301, "Samsung Curved LED", 80000, "Samsung", "OLED", 50)

sRef.showShoeDetails()

print()

mRef.showMobileDetails()

print()

lRef.showLEDTvDetails()

"""
# Common Code is Generalized as Product
class Product:

    def __init__(self, pid, name, price, brand):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand


    def updateProductDetails(self, pid, name, price, brand):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand

    def showProductDetails(self):
        print("======Product Details=====")
        print(self.pid)
        print(self.name)
        print(self.price)
        print(self.brand)
        print("=======================")

class Shoe(Product): #IS-A Relation | Shoe IS-A Product | Inheritance

    def __init__(self, color, size):
        self.color = color
        self.size = size

    def updateShoeDetails(self, pid, name):
        self.color = color
        self.size = size

    def showShoeDetails(self):
        print("======Shoe Details=====")
        print(self.color)
        print(self.size)
        print("=======================")

class Mobile(Product):

    def __init__(self, pid, name, price, brand, ram, memory):
        Product.__init__(self, pid, name, price, brand)
        self.ram = ram
        self.memory = memory

    def updateMobileDetails(self, pid, name, price, brand, ram, memory):
        Product.updateProductDetails(self, pid, name, price, brand)
        self.ram = ram
        self.memory = memory

    # Overriding
    def showProductDetails(self):
        Product.showProductDetails(self)
        print("======Mobile Details=====")
        print(self.ram)
        print(self.memory)
        print("=======================")

class LEDTv(Product):

    def __init__(self,technology, screenSize):
        self.technology = technology
        self.screenSize = screenSize

    def updateLEDTvDetails(self, technology, screenSize):
        self.technology = technology
        self.screenSize = screenSize

    def showLEDTvDetails(self):
        print("======LEDTv Details=====")
        print(self.technology)
        print(self.screenSize)
        print("=======================")

mRef = Mobile(201, "iPhoneX", 60000, "Apple", 4, 128)
mRef.showProductDetails()
