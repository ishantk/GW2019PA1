johnsAge = 30
print(johnsAge, hex(id(johnsAge)))

jenniesAge = 30
print(jenniesAge, hex(id(jenniesAge)))

# Copy Operation : Not Data Copy But Reference Copy
jacksAge = johnsAge
print(jacksAge, hex(id(jacksAge)))


# del johnsAge
# print(jenniesAge, hex(id(jenniesAge)))

# PS: johnsAge and jenniesAge are known as Reference Variables



