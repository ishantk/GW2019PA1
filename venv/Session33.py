import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

print(">> TensorFlow Version is:",tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print(len(train_images))
print(len(test_images))

print()

print(len(train_labels))
print(len(test_labels))

print("===Training Image 0 ===")
print(train_images[0])
print(class_names[train_labels[0]]) # 0 - 9

print()

print("===Testing Image 0 ===")
print(test_images[3])
print(class_names[test_labels[3]])  # 0 - 9

# plt.subplot(2, 4, 1)
# plt.imshow(train_images[0], cmap=plt.cm.gray_r)
#
# plt.subplot(2, 4, 2)
# plt.imshow(test_images[3], cmap=plt.cm.gray_r)

# plt.show()

# Create Your  Own DataSet for Dogs and Cats
# https://www.kaggle.com/dhainjeamita/dogs-and-cats-image-classification

# Break your data point values into range of 0 to 1 (Fuzzy DataSet)
train_images = train_images / 255.0
test_images = test_images / 255.0

# Create Model -> ANN :)
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(32, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

# Compile Your Model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Training the Model iteratively !!
model.fit(train_images, train_labels, epochs=5)


# Errors :) | Desired Output Vs Actual Output
# Check for Loss and Accuracy Parameters
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)

# Make Prediction
predictions = model.predict(test_images)
print(len(predictions))
print(predictions[3])
print(len(predictions[3])) # 10 probabilities :)

idx = np.argmax(predictions[3])
print(">> Max Probability:", idx)

plt.subplot(2, 4, 2)
plt.imshow(test_images[3], cmap=plt.cm.gray_r)
plt.title(class_names[idx])
plt.show()



