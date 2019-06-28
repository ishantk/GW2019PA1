import matplotlib.pyplot as plt

"""
A = [1, 2, 3, 4, 5]
B = [10, 20, 30, 15, 60]

plt.bar(A, B)
plt.show()
"""

scores = {"virat":82, "rohit":140, "rahul":102, "dhawan":118, "dhoni":56}

"""
plt.bar(0, scores["virat"])
plt.bar(1, scores["rohit"])
plt.bar(2, scores["rahul"])
plt.bar(3, scores["dhawan"])
plt.bar(4, scores["dhoni"])
"""

for i, key in enumerate(scores):
    # plt.bar(i, scores[key])
    plt.bar(key, scores[key])

plt.xlabel("BatsMen")
plt.ylabel("Score")
plt.title("Indian Batting")

plt.show()