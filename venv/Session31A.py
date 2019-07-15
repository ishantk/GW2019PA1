import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, svm, metrics

digits = datasets.load_digits()
# Printing the entire data set
# print(digits)

# Image Data as Numpy Array
# print(digits.images)
# print(digits['images'])

# Target Digits i.e. Labels of Different Classes
# print(digits.target)
# print(digits['target'])


"""
print(digits['images'][0])          # Input
print(digits['images'][0].shape)
print(digits['target'][0])          # Output Label

print(digits['images'][1])          # Input
print(digits['images'][1].shape)
print(digits['target'][1])          # Output Label
"""


"""
plt.subplot(2, 4, 1)
plt.imshow(digits.images[0], cmap=plt.cm.gray_r)

plt.subplot(2, 4, 2)
plt.imshow(digits.images[1], cmap=plt.cm.gray_r)

plt.show()
"""


for i in range(1, 5):
    plt.subplot(2, 4, i)
    plt.imshow(digits.images[i], cmap=plt.cm.gray_r)

plt.show()


print("==Input==")
print(digits.images)
print(len(digits.images))
print()
print("==Labels==")
print(digits.target)
print(len(digits.target))
print("==Classes==")
print(digits.target_names)

X = digits.data
Y = digits.target

model = svm.SVC(gamma='scale')
model.fit(X, Y)

inputSample = digits.data[4]

predictedClass = model.predict([inputSample])

print(">> Predicted Class is:",predictedClass)

# Assignment:
# https://gogul09.github.io/software/image-classification-python



