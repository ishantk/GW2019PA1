data = [1, 2, 3, 4, 5]
# length = len(data)
# print(length)
print(len(data))
print(max(data))
print(min(data))

print()
print("======")
# Iterate in list
for i in range(len(data)):
    print(data[i])

print("======")
print()

# Enhanced For Loop / For-Each Loop
for elm in data:
    print(elm)
print("======")

print([x**2 for x in data])

numbers = list(range(1, 101, 3))
print(numbers)

