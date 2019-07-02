import pandas as pd
import numpy as np

data = np.random.rand(5, 4)
# print(data)

frame = pd.DataFrame(data, columns=["COL1", "COL2", "COL3", "COL4"])
print(frame)
print("-------")
print(frame["COL1"])
print("-------")

# Iterate using iteritems function: Columns
for key, value in frame.iteritems():
    print(key)
    print("--------")
    print(value)
    print(type(value))
    print(">>>>>>>>>>>>>>>>>")

# Conclusion : DataFrame is collection of Series
#              Series is a collection of numpy ndarray

print("#@#@#@#@#@#@#@#@#@#@")

# Iterate using iterrows function: Rows
for key, value in frame.iterrows():
    print(key)
    print("--------")
    print(value)
    print("*****************")

print("$&$&$&$&$&$&$&$&$&$&")

# Iterate using itertuples function: Returns row as a Tuple
for row in frame.itertuples():
    print(row)
    print("^^^^^^^^^^^^^^^^^^")
