"""
    XOR
    A   B   Y
    0   0   0
    0   1   1
    1   0   1
    1   1   0

    A XOR B is:
   (A OR B)  AND  ( NOT (A AND B))
   (1 OR 1) AND (NOT (1 AND 1))
   1    AND     ( 0 )
   0
"""
import numpy as np

def activation(s):  # Binary Unit Step :)
    if s >= 1:
        return 1
    else:
        return 0

def activationNOT(s):  # Binary Unit Step :)
    if s >= -0.5:
        return 1
    else:
        return 0

def summation(x, w):
    s = np.dot(x, w)
    y = activation(s)
    return y

def summationNOT(x, w):
    s = x * w
    y = activationNOT(s)
    return y

input1 = np.array([0, 0])
input2 = np.array([0, 1])
input3 = np.array([1, 0])
input4 = np.array([1, 1])

weightsAND = np.array([0.5, 0.5])
weightsOR = np.array([1.1, 1.1])
weightNot = -1

ao1 = summation(input1, weightsAND)
ao2 = summation(input2, weightsAND)
ao3 = summation(input3, weightsAND)
ao4 = summation(input4, weightsAND)

oo1 = summation(input1, weightsOR)
oo2 = summation(input2, weightsOR)
oo3 = summation(input3, weightsOR)
oo4 = summation(input4, weightsOR)

noo1 = summationNOT(ao1, weightNot)
noo2 = summationNOT(ao2, weightNot)
noo3 = summationNOT(ao3, weightNot)
noo4 = summationNOT(ao4, weightNot)

print(ao1, ao2, ao3, ao4)
print(oo1, oo2, oo3, oo4)
print(noo1, noo2, noo3, noo4)

input1 = np.array([oo1, noo1])
input2 = np.array([oo2, noo2])
input3 = np.array([oo3, noo3])
input4 = np.array([oo4, noo4])


o1 = summation(input1, weightsAND)
o2 = summation(input2, weightsAND)
o3 = summation(input3, weightsAND)
o4 = summation(input4, weightsAND)

print(o1, o2, o3, o4)

# Assignment : Do it with OOPS :)

