# import json as js
import json # Java Script Object Notation

employee = {"eid":101, "name":"John", "salary":30000}
print(employee)
print(type(employee))

print()

# Convert Dictionary into JSON
# JSON is a textual i.e. String representation of Dictionary

jsonData = json.dumps(employee)
print(jsonData)
print(type(jsonData))

print()

# jsonData = str(employee)
# print(jsonData)
# print(type(jsonData))

# Get the json data i.e. string format of dictionary
# and convert it into Dictionary

dictData = json.loads(jsonData)
print(dictData)
print(type(dictData))