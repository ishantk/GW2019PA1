import torch
import numpy as np

print(">> Torch Version:",torch.__version__)

X = torch.empty(5, 3)
print(X)
print(type(X)) # Tensor -> is n-D Array in PyTorch and TensorFlow

print()

X = torch.rand(3, 3)
print(X)

print()

X = torch.zeros(5, 5)
print(X)

print()

X = torch.zeros(5, 5, dtype=torch.int)
print(X)

print()

# Python List
numbers = [10, 20, 30, 40, 50]
print(numbers)

# Creating a PyTorch Tensor from Python List
torchTensor = torch.tensor(numbers)
print(torchTensor)

ndArr = torchTensor.numpy()
print(ndArr)

# Convert numpy Array to Pytorch tensor
data = np.array([1, 3, 5, 7, 9])
print(data)

torchData = torch.from_numpy(data)
print(torchData)

# Start Exploring : https://pytorch.org/tutorials/
# https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py
##############################
# https://chsasank.github.io/
##############################
