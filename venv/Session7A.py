"""

    Object Oriented Programming Structure
    OOPS
    > Object
    > Class

        1. Encapsulation
        2. Abstraction
        3. Inheritance
        4. Polymorphism

    Real World:
        Object : is anything which you can see and touch
                 Which is Real -> Real Time Entity

        Class  : is drawing of an object
                 is representation how an object will look like

        What will you think of first ??
        OOPS Principle
        1. Think of an Object
        2. Draw Object
        3. Create Real Object by looking Drawing

    Computer Science:
        Object : Multi Value Container
                If we wish to customize MVC we will create Objects

        Class  : Is textual representation of an Object

        eg : Geometry Box
              All pencils               | Homo
            pencil, eraser, sharpner... | Hetro

            User is an Object
            User has lot of data associated with it
              name
              phone
              email
              gender
              age
              address
              .
              ..

          Identification of Object
          Requirement: User should register in my app.
          User should enter source and destinition
          location and book a cab.
          User should be allocated a Driver to complete Ride


          Model View Controller Architecture
          Model -> Object

          Driver : name, phone, email, license, experience ..
          Cab    : brand, type, color, regNum ....
          Ride   : source, desti, cab, driver, user

          Data Associated with object is attributes
"""

class User:
    pass

class Driver:
    pass

data = []
print(type(data))

# 1. Object Construction Statement
u = User()
v = User()

d = Driver()

print(type(u))
print(type(v))
print(type(d))

print(u)
print(v)
print(d)

# 2. Write Data in Object
u.name = "John"
u.phone = "+91 99999 88888"
u.email = "john@example.com"
u.address = "Redwood Shores"

v.name = "Fionna"
v.age = 30
v.salary = 30000

# reference copy
w = v

print(w)

d.name = "George"
d.phone = "+91 77777 88888"
d.experience = 3
d.licence = "PBX3412"

# 3. Update Operation in Object
u.name = "John Watson"
w.age = 33

# 4. Delete Operation in Object
del u.phone
del d.licence

# 5. Read operation on Object
print(u.__dict__)
print(v.__dict__)
print(d.__dict__)