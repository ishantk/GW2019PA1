class Product:

    # Property of Class
    restaurantName = "ABC"

    # Constructor : When Object will be created in memory
    # def __init__(self):
    #     self.name = "Dal Makhani"
    #     self.price = 200

    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Function
    def showProduct(self):
        print(self.name, self.price, Product.restaurantName)

    # Destructor : When Object will be deleted form memory
    def __del__(self):
        print("Product Deleted", self)

p1 = Product("Paneer", 200)
p2 = Product("Dal", 100)

print(hex(id(p1)))
print(hex(id(p2)))

print(p1.__dict__)
print(p2.__dict__)

p1.showProduct()
p2.showProduct()

del p1

print("Thank You")