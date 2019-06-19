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

    6. Update Data in Table
    update Customer set name = 'John Watson', email = 'john.w@example.com', phone = '+91 99999 88888' where cid = 1

    7. Delete Data in Table
    delete from Customer where cid = 1

    8. fetch all rows from Table in Database
    select * from Customer

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

    def updateCustomerInDB(self, customer):

        # 1. Create SQL Statement
        sql = "update Customer set name = '{}', email = '{}', phone = '{}' where cid = {}".format(customer.name, customer.email, customer.phone, customer.cid)
        # 2. Create Connection with Database
        con = mysql.connector.connect(user="root", password="",host="127.0.0.1", database="auridb")

        # 3. Obtain Cursor ro execute SQL Statements
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

        print(customer.name," Updated !!")

    def deleteCustomerInDB(self, cid):
        # 1. Create SQL Statement
        sql = "delete from Customer where cid = {}".format(cid)
        # 2. Create Connection with Database
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="auridb")

        # 3. Obtain Cursor ro execute SQL Statements
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

        print(cid, " Deleted !!")

    def fetchAllCustomers(self):
        # 1. Create SQL Statement
        # sql = "select * from Customer"
        # sql = "select * from Customer order by name asc"
        sql = "select * from Customer order by name desc"

        # 2. Create Connection with Database
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="auridb")

        # 3. Obtain Cursor ro execute SQL Statements
        cursor = con.cursor()
        cursor.execute(sql)

        # row = cursor.fetchone()
        # print(row)
        #
        # row = cursor.fetchone()
        # print(row)

        rows = cursor.fetchall()
        # print(rows)  # rows is a List of Tuples. 1 Tuple Represents 1 Row

        for row in rows:
            print(row)

    def fetchCustomer(self, cid):
        # 1. Create SQL Statement
        sql = "select * from Customer where cid = {}".format(cid)

        # 2. Create Connection with Database
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="auridb")

        # 3. Obtain Cursor ro execute SQL Statements
        cursor = con.cursor()
        cursor.execute(sql)

        row = cursor.fetchone()
        print(row)

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
print("2. Update Customer")
print("3. Delete Customer")
print("4. View All Customers")

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

elif choice == 2:

    db = DBHelper()

    cRef = Customer(None, None, None)
    cRef.cid = int(input("Enter Customer ID:")) # we need to know which id has to be updated !!

    db.fetchCustomer(cRef.cid)


    cRef.name = input("Enter Customer Name:")
    cRef.phone = input("Enter Customer Phone:")
    cRef.email = input("Enter Customer Email:")

    cRef.showCustomerDetails()

    update = input("Would you like to Update Customer(yes/no)")
    if update == "yes":
        db.updateCustomerInDB(cRef)

elif choice == 3:

    cid = int(input("Enter Customer ID:"))

    delete = input("Would you like to Delete Customer(yes/no)")
    if delete == "yes":
        db = DBHelper()
        db.deleteCustomerInDB(cid)

elif choice == 4:
    db = DBHelper()
    db.fetchAllCustomers()
