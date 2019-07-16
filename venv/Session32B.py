from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

irisData = load_iris()

FEATURES = irisData.data

print(FEATURES)


clusters = 3
model = KMeans(n_clusters=clusters)

# train the model
# we are not mentioning labels :)
model.fit(FEATURES)

predictions = model.predict(FEATURES)
print(predictions)

# Use Clustering on Image DataSets :)