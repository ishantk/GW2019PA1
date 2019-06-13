class Order:

    def __init__(self, oid, price, restaurantName):
        self.oid = oid                          # Public
        self._price = price                     # Protected
        self.__restaurantName = restaurantName  # Private -> NAME MANGLING

    def __showOrder(self):
        print(self.oid, self._price, self.__restaurantName)

o1 = Order(101, 3000, "ABC Masala")
# print(o1.__dict__)
# print(o1.oid)
# print(o1._price)
# print(o1._Order__restaurantName)

o1._Order__showOrder()
print(o1.__dict__)
print(Order.__dict__)

# Sorting Algorithms : GeekforGeeks
# Implement Different Algorithms on List
