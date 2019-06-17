file = open("Session11E.py", "r")
data = file.read(15)
print(data)
print("=========")
data = file.read(30)
print(data)

print("=========")
data = file.read()
print(data)

print("Is File Closed:",file.closed)

file.close() # Explicitly we are closing the file

print("Is File Closed:",file.closed)