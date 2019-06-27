import numpy as np
arr = np.loadtxt("data.txt")
print(arr)


print("========")

# 1-D Array | Try out 2D and 3D Arrays as well
arr = np.arange(10, 200, 10)
print(arr)
# np.savetxt("arraydata.txt", arr)
np.savetxt("arraydata1.txt", arr, fmt="%04d")
print("==Data Written==")
