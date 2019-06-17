file = open("/Users/ishantkumar/Downloads/MyApp.py","r")
"""
line = file.readline()
print(line)
line = file.readline()
print(line)
line = file.readline()
print(line)
line = file.readline()
print(line)
line = file.readline()
print(line)
"""
# readline will read a single line
# and next time it will read the next line

lines = file.readlines()
print(lines)
print(type(lines)) # List -> List of all the lines in a file

for line in lines:
    print(line)
