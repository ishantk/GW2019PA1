name = "John Watson"
print(name, type(name), hex(id(name)))
print(len(name))
print("Max:",max(name))
print("Min:",min(name))

print(name[1])
print(name[len(name)-1])

print(name[1:3])
print("t" in name)

email = "john@example.com"

if ("@" in email) and ("." in email):
    print("Valid Email")
else:
    print("Invalid Email")

# Create a Program to Test a Member in a Sequence
# Your program should work on List, Tuple, String