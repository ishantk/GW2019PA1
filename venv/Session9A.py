"""
    Relationship Mapping

        HAS-A Mapping

        1 Engineer working on 1 Project
        1  Engineer working on Many Projects
        Many Engineers working on Many Projects

        1 Customer has 1 Address
        1 Customer has many Addresses
        Many Customers have Many Addresses

        Customer
            name
            phone
            email
        Address
            adrsLine
            city
            state
"""

class Customer:

    # Constructor for Standardization
    # def __init__(self, name, phone, email, address):
    #     self.name = name
    #     self.phone = phone
    #     self.email = email
    #     self.address = address # HAS-A | 1 to 1

    def __init__(self, name, phone, email, addresses):
        self.name = name
        self.phone = phone
        self.email = email
        self.addresses = addresses # HAS-A | 1 to many

    # Function : Update Operation
    def updateCustomerDetails(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    # Function : Read Operation
    def showCustomerDetails(self):
        print("=================")
        print("Name:\t",self.name)
        print("Phone:\t", self.phone)
        print("Email:\t", self.email)
        print("=================")

        print(">> Address List for {}:".format(self.name))

        # self.address.showAddressDetails() # 1 to 1
        for adrs in self.addresses:         # 1 to *
            adrs.showAddressDetails()

        print(">>>>>>>>>>>>>>>>>>>>")

    # Business Function : Will have logical processing (Controller)
    def getTotalAddresses(self):
        return len(self.addresses)


    # def __del__(self):
    #     print("This is optional as per requirement")

class Address:

    # Constructor for Standardization
    def __init__(self, adrsLine, city, state):
        self.adrsLine = adrsLine
        self.city = city
        self.state = state

    # Function : Update Operation
    def updateAddressDetails(self, adrsLine, city, state):
        self.adrsLine = adrsLine
        self.city = city
        self.state = state

    # Function : Read Operation
    def showAddressDetails(self):
        print("=================")
        print("AdrsLine:\t",self.adrsLine)
        print("City:\t", self.city)
        print("State:\t", self.state)
        print("=================")


adrsList = []
choice = "yes"
while choice == "yes":
    adrs = Address(None, None, None)
    adrs.adrsLine = input("Enter Address Line: ")
    adrs.city = input("Enter City: ")
    adrs.state = input("Enter State: ")
    adrsList.append(adrs)

    choice = input("Would you like to add another Address(yes/no): ")

"""
a1 = Address(None, None, None)
a1.adrsLine = input("Enter Address Line: ")
a1.city = input("Enter City: ")
a1.state = input("Enter State: ")


a2 = Address("Country Homes", "Ludhiana", "Punjab")

# List of Addresses
adrsList = [a1, a2]
"""
# c1 = Customer("John", "+91 99999 88888", "john@example.com", a1)
c1 = Customer("John", "+91 99999 88888", "john@example.com", adrsList)

# c1.showCustomerDetails()

cRef = c1
cRef.showCustomerDetails()

# a1.showAddressDetails()
# a2.showAddressDetails()

"""
    1 Order Can Have Many FoodItems
    With User Input Create a small program ;) ;)
    With User input add as many as FoodItems in the list called cart
    Create a function in Order class -> getTotalAmount() which return total
    Create a function applyPromoCode in Order class -> applyPromoCode() which returns a discounted price
    
    oRef = Order()
    print(oRef.getTotalAmount())
    print(oRef.applyPromoCode(inputs))
    oRef.showSortedFoodItems() # Based on Price of FoodItem Asc
    
    class FoodItem:
        pass
    
    class Order:
        def getTotalAmount(self):
            pass
            
        def applyPromoCode(self):
            pass
            
        def showSortedFoodItems(self):
            pass 
"""