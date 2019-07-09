from sklearn.datasets import load_iris
from  sklearn import tree

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
model = tree.DecisionTreeClassifier()

# 3. Train the Model | Supervised Learning
model.fit(irisData.data, irisData.target)

# 4. Lets Test our Model !!
inputData = [5.5, 2.6, 4.4, 1.2] # -> Versicolor Type of Iris Flower

predictedClass = model.predict([inputData])

print()

# print(">> Predicted Flower Type is:",predictedClass)
# print(">> Predicted Flower Type is:",predictedClass[0])
print(">> Predicted Flower Type is:",irisData.target_names[predictedClass[0]])

# Export our Data as Graph Visual !!
import graphviz
data = tree.export_graphviz(model, out_file=None)
graph = graphviz.Source(data)
graph.render("IRIS DATASET TREE")
graph.view()

# Explore : Gini Index and Chi Square w.r.t. Tree
# Analyze What can be type of Flu/Malarias/Diabetes etc...