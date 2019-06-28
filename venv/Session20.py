# Code Data Analysis and Machine Learning Online
# https://jupyter.org/try
import pandas as pd

numbers = [11, 22, 33, 44, 55]
s1 = pd.Series(numbers)

print(s1)

print()

ages = {"john":20, "jennie":30, "jim":40, "jack":50, "joe":60}
s2 = pd.Series(ages)

print(s2)

# Access Elements:
print(s1[0])
print(s2["jennie"])

# Slice Elements:
print(s1[1:])
print(s1[:3])
print(s1[2:5])

print(s2["jim":])
print(s2["jim":"joe"]) # jim and joe will be inclusive