"""
names = ["John", "Fionna", "Kia"]
names[0] = "John Watson"
print(names)
"""

# IMMUTABLE
names = ("John", "Fionna", "Kia")
# names[0] = "John Watson"
# names.append("Kim")
print(names)

# Converted Tuple into list
newNames = list(names)
print(newNames, type(newNames))

# HW: Session4A till last: Explore on Tuples and Sets