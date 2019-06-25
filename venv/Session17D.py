import re

quote = "Work Hard and Get Luckier"
data = re.findall(".", quote)
print(data)

print()

data = re.findall("\w", quote)
print(data)

print()

data = re.findall("\w*", quote)
print(data)

print()

data = re.findall("\w+", quote)
print(data)

# With Regular Expression Validate:
# Assignment : Validate Vehicle Number
# vehicleNumber = "PB10AB1234"
