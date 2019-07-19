# Dimensionality Reduction
# We shall optimize our dataset with the features which are required
# We have mathematical Algorithms to do so !!

from sklearn.feature_selection import VarianceThreshold

# feature_selection
# feature_extraction

X = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
        [0, 1, 1],
        [0, 1, 0],
        [0, 1, 1]
    ]
print(X) # Print Before
print()

reduction = VarianceThreshold(.8 * (1-.8))
X = reduction.fit_transform(X)

print(X) # Print After
