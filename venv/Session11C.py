"""
    object
  int  str  Customer
            PrimeCustomer



"""

# class CA:
# class CA():
class CA(object):
    pass

"""
class CB(CA):
    pass

class CC(CB):
    pass
"""
cRef = CA()
print("Object Data:",cRef.__dict__)
print("CA Class Data:", CA.__dict__)
# print("CB Class Data:", CB.__dict__)
# print("CC Class Data:", CC.__dict__)

a = 10
a = "John"
a = CA()