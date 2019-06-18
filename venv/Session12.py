"""
    DataBase : MySQL
    Prog Lang : SQL -> Structured Query Language

    Relational DataBase management System | RDBMS

    1. Create DataBase
        DataBase is collection of Tables
        Tables can be related to each other : 1 to 1 or 1 to many | has-a or is-a

    2. Create Table in DataBase
        Table is a collection of rows and columns eg: excel sheet

        ORM : Object Relational Mapping
        Your Object's Attributes should be Table's Column Names
        But in Table we can have 1 additional column and we call it as Primary Key and Auto Increment
        1 2 3 4 5 6....

        class Customer:
            def __init__(self, name, phone, email):
                self.name = name
                self.phone = phone
                self.email = email

        create table Customer(
            cid int primary key auto_increment,
            name varchar(256),
            phone varchar(20),
            email varchar(256)
        )

    3. Insert Data in Table
    cRef = Customer('John', '+91 99999 88888', 'john@example.com')
    insert into Customer values(null, 'John', '+91 99999 88888', 'john@example.com')

    4. Install Library mysql-connector

    5. Create a DBHelper which will be accessing database

"""

import mysql.connector


# DAO : Data Access Object
class DBHelper:

    def saveCustomerInDB(self, customer):

        # 1. Create SQL Statement
        sql = "insert into Customer values(null, '{}', '{}', '{}')".format(customer.name, customer.phone, customer.email)

        # 2. Create Connection with Database
        con = mysql.connector.connect(user="root", password="",host="127.0.0.1", database="auridb")

        # 3. Obtain Cursor ro execute SQL Statements
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

        print(customer.name," Saved !!")

# Model
class Customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomerDetails(self):
        print(">> Name: {} Phone: {} Email:{}".format(self.name, self.phone, self.email))

print("Options:")
print("1. Create New Customer")

choice = int(input("Enter Choice: "))

if choice == 1:
    cRef = Customer(None, None, None)
    cRef.name = input("Enter Customer Name:")
    cRef.phone = input("Enter Customer Phone:")
    cRef.email = input("Enter Customer Email:")

    cRef.showCustomerDetails()

    save = input("Would you like to save Customer(yes/no)")
    if save == "yes":
        db = DBHelper()
        db.saveCustomerInDB(cRef)



