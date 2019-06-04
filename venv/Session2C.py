dishPrice = 100
# dishesPrices = 100, 200, 350, 500, 120
dishesPrices = (100, 200, 350, 500, 120)    # Homogeneous
anotherDishesPrices = (100, 200.22, 350, 500, 120, "100") # Hetrogeneous


print(dishPrice, hex(id(dishPrice)), type(dishPrice))
print(dishesPrices, hex(id(dishesPrices)), type(dishesPrices))

print(dishesPrices[0], hex(id(dishesPrices[0])), type(dishesPrices[0]))