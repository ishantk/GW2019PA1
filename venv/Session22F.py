import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# Explore Seaborn: https://seaborn.pydata.org/


table = pd.read_csv("soccerdata.csv")
# print(table)

# print(table.head(5))
# print(table.tail(5))

# print(table["Name"])
# print(table.Name)

# Take some less samples to plot and check
# sns.countplot(y=table.Nationality, palette="Set2")
# plt.show()

# sns.countplot(x="Age", data=table)
# plt.show()


# Case Study : Find the GoalKeeper who is strongest to stop the shots
# print(table["GK_Handling"])

# Let us create weights for attributes
w1 = 1
w2 = 2
w3 = 3
w4 = 4

table["Best_GoalKeepers"] = (w1 * table.GK_Positioning + w2 * table.GK_Diving + w3 * table.GK_Handling + w4 * table.GK_Reflexes)
print(table["Best_GoalKeepers"])

sortedData = table.sort_values("Best_GoalKeepers")
# print(sortedData)

print("===============")
print(sortedData.head(5))
print("===============")
print(sortedData.tail(5))
print("===============")


# Assignment
# Fetch Data from espn cric info and analyze world cup stats :)
