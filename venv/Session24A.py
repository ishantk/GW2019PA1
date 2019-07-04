import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

"""
    ======================
    Final Equation of Line
    ======================
    Y = 2.2 + (0.6)X
    ====================== 
"""

data = stats.linregress(X, Y)

print("Slope of Line", data[0])
print("Intercept of Line", data[1])


maxX = np.max(X) + 10
minX = np.min(X) - 10
x = np.linspace(minX, maxX, 100)
y = data[1] + data[0]*x

"""
print(x)
print("********")
print(y)
"""

plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
# plt.plot(X, Y, "o")
plt.plot(x, y, color="r", label="Regression Line")
plt.scatter(X, Y, color="b", label="Data Points")
plt.legend()
plt.show()
