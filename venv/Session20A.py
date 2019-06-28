import pandas as pd

nums1 = [10, 20, 30, 40, 50]
nums2 = [11, 22, 33, 44, 55]

emp1 = {"eid":101, "name":"John", "age":20}
emp2 = {"eid":201, "name":"Fionna", "age":22}
emp3 = {"eid":301, "name":"Kia", "age":24}

df1 = pd.DataFrame([nums1, nums2])
df2 = pd.DataFrame([emp1, emp2, emp3])

print(df1)
print()
print(df2)

# We will be getting columns instead of Rows below:
print()
print(df1[0])
print()
print(df2["eid"])

print()
print(df2["eid"][1])
print(df2["name"][1])
print(df2["age"][1])
