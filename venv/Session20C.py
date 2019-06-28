import matplotlib.pyplot as plt
"""
f(X) = X
X : 1
X : 2

Y = f(X)

"""

"""
# Assuming X is index in the List Y
# 0, 1, 2, 3, 4
Y = [10, 2, 300, 210, 50]
plt.plot(Y)
plt.show()
"""

X = list(range(1,11))

# List Comprehension
Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]

print(X)
print(Y1)
print(Y2)
print(Y3)

plt.plot(X, Y1, label="Y1")
plt.plot(X, Y2, label="Y2")
plt.plot(X, Y3, label="Y3")

plt.legend() # How can we place legend on different positions -> Explore

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.title("Polynomial Graphs")
plt.grid(True)

# plt.xlim(0, 300)
# plt.ylim(0, 3000)

# To Save Graph
# plt.savefig("MyGraph")

plt.show()




