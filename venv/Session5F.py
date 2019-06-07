S1 = {1, 2, 3, 'a', 'b'}
S2 = {1, 'a', 'b'}

print(1 in S1)

print(S2.issubset(S1))
print(S1.issuperset(S2))

print("S1 before is:",S1)
print(S1.union(S2))
print("S1 now is:",S1)

print(S1.intersection(S2))
print(S1.difference(S2))

# print(S1.symmetric_difference(S2))

# Explore -> symmetric difference