# Bitwise operators

a = 8       # 1 0 0 0
b = 12      # 1 1 0 0
c = a & b   # 1 0 0 0
d = a | b   # 1 1 0 0
e = a ^ b   # 0 1 0 0
print(c)    #
print(d)    #
print(e)    #

"""
x = 12      # 1 1 0 0
y = 3
# Right Shift Operation
# z = x >> y  # 1 1 0 0 >> 3 -> 0 0 0 1
z = x << y    # 1 1 0 0 << 3 -> 1 1 0 0 0 0 0
print(z)      
"""
# x = -11             # 1 0 1 1
x = -13
y = 2               # _ _ 1 0
z = x >> y          # 2
print("z is:",z)

# 1 0 1 1   +11
# 0 1 0 0
#       1
# 0 1 0 1   2s Complement
# _ _ 0 1
# 1 1 0 1
# 0 0 1 0
#       1
# 0 0 1 1 -> -3



