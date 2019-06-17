class Order:

    def __init__(self, oid, customerName, dishCount, price):
        self.oid = oid
        self.customerName = customerName
        self.dishCount = dishCount
        self.price = price

    def toCSV(self):
        return "{},{},{},{}\n".format(self.oid, self.customerName, self.dishCount, self.price)

"""
orders = []
choice = "yes"

while choice == "yes":
    pass
"""

o1 = Order(1, "John", 3, 450)
o2 = Order(2, "Jennie", 5, 750)
o3 = Order(3, "Jim", 7, 1450)

# print(o1.__dict__)
# print(o2.__dict__)
# print(o3.__dict__)

print(o1.toCSV())
print(o2.toCSV())
print(o3.toCSV())



# Persistance : Store/Save the data of an Object Permanently somewhere
# 1. Files
# 2. Data Base -> SQL / No SQL


file = open("/Users/ishantkumar/Downloads/Orders.csv", "a")
file.write(o1.toCSV())
file.write(o2.toCSV())
file.write(o3.toCSV())

print(">> Orders Saved !!")

# Read the same file and :
# 1. Find order with maximum number of dishes
# 2. Find Order with maximum Value
# 3. Read the file and recreate a new file with sorted orders based on price :)

