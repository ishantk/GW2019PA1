import matplotlib.pyplot as plt

trends = [51, 26, 86]
domains = ["Java", "Python", "C++"]

plt.pie(trends, labels=domains)
plt.legend()
plt.show()