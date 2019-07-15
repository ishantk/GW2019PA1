from sklearn import svm

"""
# Input Data
X = [[0, 0], [1, 1]]

# Label
Y = [0, 1]


model = svm.SVC(gamma='scale')
model.fit(X, Y)

inputSample = [2, 2]
predictedClass = model.predict([inputSample])
print(">> Predicted Class is:",predictedClass)
"""

# Representation of Data
data = [ [100, 100],
         [150, 110],
         [180, 150],
         [200, 180],
         [800, 1000],
         [1000, 1200],
         [1200, 1300],
         [1500, 1500],
       ]

labels = [0, 0, 0, 0, 1, 1, 1, 1]

model = svm.SVC(gamma='scale')
model.fit(data, labels)

inputSample = [100, 170]
predictedClass = model.predict([inputSample])
print(">> Predicted Class is:",predictedClass)