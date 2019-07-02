# Explore Web Crawling: https://scrapy.org/
import pandas as pd
import numpy as np

# arr = np.arange(1, 51, 2)
arr = list(range(1, 51))
S1 = pd.Series(arr)
print("----------")
print(S1)
print("----------")
print(S1.axes)
print("----------")
data = S1.values
print(data)
print(type(data))
print("----------")
print(S1.head(5))
print("----------")
print(S1.tail(5))