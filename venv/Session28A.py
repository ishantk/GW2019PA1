# Explore iris data set with Naive Bayes :)
# Links to Data Sets
# https://data.gov.in/
# https://github.com/jbrownlee/Datasets
# Create account on https://app.chime.aws/

from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

# 1. Lets Create Data Set
irisData = load_iris()
print("===IRIS DATASET===")
print(irisData)
print(type(irisData))

print()

# Array of Features :)
print("===IRIS DATA FEATURES===")
print(irisData.data)

print()

# Array of Targets
print("===IRIS DATA TARGET===")
print(irisData.target)

print()

# Array of Target Names
print("===IRIS DATA TARGET NAMES===")
print(irisData.target_names)

# 2. Lets Create Model
model = GaussianNB()

# 3. Train the Model | Supervised Learning
model.fit(irisData.data, irisData.target)

# 4. Lets Test our Model !!
inputData = [5.5, 2.6, 4.4, 1.2] # -> Versicolor Type of Iris Flower

predictedClass = model.predict([inputData])

print(">> Predicted Flower Type is:",irisData.target_names[predictedClass[0]])
