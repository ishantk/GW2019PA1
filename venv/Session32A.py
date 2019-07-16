from sklearn.cluster import KMeans

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

# Lets do not keep any labels for our data
# and k means clustering should do the labeling for us
# labels = [0, 0, 0, 0, 1, 1, 1, 1]

targetNames = ["Car", "Bike"]

clusters = 2
model = KMeans(n_clusters=clusters)

# train the model
# we are not mentioning labels :)
model.fit(data)

# predictions = model.predict(data)
# print(predictions)


sampleInput = [800, 1000]
predictedClass = model.predict([sampleInput])
print(predictedClass)