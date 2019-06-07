# String Formatting
name = "Fionna"
age = 30
print("Welcome to our Club %s"%(name))
print("Your Age is: %d"%(age))

print("Hey, %s You are %d years old"%(name, age))
print("Hey,",name,"You are",age,"years old")

print("Hey, {} You are {} years old".format(name, age))

number = 7
for i in range(1, 11):
    print("{} {}'s are {}".format(number, i, number*i))