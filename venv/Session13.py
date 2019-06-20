# tkinter to create GUI's
from tkinter import *

# import Session12
# from Session12 import Customer
# from Session12 import DBHelper

from Session12 import *

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


# cRef = Session12.Customer("John", "+91 99999 88888", "john@example.com")
# cRef.showCustomerDetails()

def onClick():

    print("Button Clicked")

    cRef = Customer(None, None, None)

    cRef.name = entryName.get()
    cRef.phone = entryPhone.get()
    cRef.email = entryEmail.get()

    cRef.showCustomerDetails()

    # db = DBHelper()
    # db.saveCustomerInDB(cRef)

    data = cRef.__dict__

    db.collection("Customer").document().set(data)

    print(">> ", cRef.name, "Saved in Firebase")


window = Tk()

lblTitle = Label(window, text="Add Customer Details")
lblTitle.pack()

lblName = Label(window, text="Enter Customer Name")
lblName.pack()

entryName = Entry(window)
entryName.pack()

lblPhone = Label(window, text="Enter Customer Phone")
lblPhone.pack()

entryPhone = Entry(window)
entryPhone.pack()

lblEmail = Label(window, text="Enter Customer Email")
lblEmail.pack()

entryEmail = Entry(window)
entryEmail.pack()

btnAddCustomer = Button(window, text="Add Customer", command=onClick)
btnAddCustomer.pack()

window.mainloop() # Keep on running the program/process

"""
    Phase-I
    CRUD Operations with GUI + Firebase :)
    
    Phase-II
    Loyalty Points : 100 -> 1Point 1Re
    > Shopping Amount should be Entered
    > 2 : 3500 | 10Percent | 350+100 = 450
    > Check Loyalty Points
    > Redeem Loyalty Points
        shopping amount > 500
        in 1 billing only 150 can be redeemed maximum
        
        
    


"""