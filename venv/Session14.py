"""
    0. Login to Google Firebase Console
    1. Create a Project on Google Firebase Console
    2. Create DataBase with test mode
    3. Create a Collection and a Document in it :)
    4. Search -> google firebase firestore python on google and click the 1st link
    https://firebase.google.com/docs/firestore/quickstart


"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Model
class Customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomerDetails(self):
        print(">> Name: {} Phone: {} Email:{}".format(self.name, self.phone, self.email))



# Use a service account
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Insert Operation
# cRef = Customer("Fionna", "+91 99999 88888", "fionna@example.com")
# data = cRef.__dict__
#
# db.collection("Customer").document().set(data)
#
# print(">> ",cRef.name,"Saved in Firebase")

docs = db.collection("Customer").get()

for doc in docs:
    print(doc.id, doc.to_dict())
