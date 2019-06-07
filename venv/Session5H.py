employee = {"name":"John", "eid":101, "email":"john@example.com", "salary":30000}
print(employee, type(employee))
print(len(employee))
print(max(employee))
print(min(employee))

employee["name"] = "John Watson" # update operation
print(employee)
print(employee["name"])

keys = list(employee.keys())
values = list(employee.values())

print(keys, type(keys))
print(values, type(values))

# In Dictionary we have Keys as Unique !!
# But Values can be duplicated
for key in keys:
    print(key, employee[key])

dishes = {"dish1":100, "dish2": 200, "dish3":300, "dish4":150}
# dishes. -> Explore more built ins :)
# Explore Dictionary in Dictionary, Set in Set
# Set in Dictionary and Dictionary in List etc etc...
