import numpy as np

arr1 = np.arange(10, 21)
print(arr1)

print()

arr2 = np.arange(10, 31, 3)
print(arr2)

# arr3 = np.ones((3,3,3), dtype=int)
arr3 = np.ones((3,3), dtype=int)
arr3[0][1] = 9
print(arr3)

print()

arr4 = np.linspace(0, 21, 4)
print(arr4)
