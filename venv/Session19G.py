import pandas as pd
import numpy as np

# List
numbers = [10, 20, 30, 40, 50]

# Numpy Array
array = np.array([11, 22, 33, 44, 55])

print(numbers)
print(array)

# Pandas Series
series = pd.Series(numbers)
print(series)

print("------")

series = pd.Series(array)
print(series)



