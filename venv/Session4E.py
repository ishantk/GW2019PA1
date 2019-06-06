cart = []

foodItem = input("Enter a Food Item of your Choice: ")

cart.append(foodItem)

print()

cart.append("sizzler")
print(cart)

print()

cart.extend(["Noodles", "Manchurian"])
print(cart)

print()

cart.insert(1, "Soya Champ")
print(cart)

print()

cart.pop(2)
print(cart)

# HW: Use all the above operations by taking inputs from User