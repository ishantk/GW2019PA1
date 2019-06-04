ages1 = (10, 20, 30, 40, 50, 60, 30)
ages2 = [10, 20, 30, 40, 50, 60, 30]
ages3 = {10, 20, 30, 40, 50, 60, 30}

print(ages1, hex(id(ages1)), type(ages1))
print(ages2, hex(id(ages2)), type(ages2))
print(ages3, hex(id(ages3)), type(ages3))

# PS: Tuple is IMMUTABLE -> Read Only
#     List is MUTABLE
#     Set is MUTABLE and UnOrdered due to Uniqueness

print(ages1[0])
# HW:
# How we will read in Set ?
# Draw Memory Representations !!