import pandas as pd
table = pd.read_csv("CityTemps.csv")
print(table)

print("================")

print(table["Year"])

print("================")

print(table.iloc[3])

print("================")

print(table.iloc[1:5])

print("=======Head 5=========")

print(table.head(5))

print("=======Tail 5=========")

print(table.tail(5))