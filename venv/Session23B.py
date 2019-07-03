# ML Algo : Everything will be Mathematical
# 1. Representation : Storage of Data
# 2. Evaluation : Algorithm to process data
# 3. Optimization : To resolve errors and make algo more stronger

"""

    1. Representation
        ** We need data first **
        Data Source can be any souce : internet i.e. html parsing
                                     : csv files from kaggle etc

        Vehicle
            Bike    :   0
            Car     :   1

           Multiple Attributes can distinguish between Bike and Car
           weight
           engine


           Data for Bikes
           100 kgs      100 cc
           150 kgs      110 cc
           180 kgs      150 cc
           200 kgs      180 cc

           Data for Car
           800 kgs      1000 cc
           1000 kgs     1200 cc
           1200 kgs     1300 cc
           1500 kgs     1500 cc


"""

from sklearn import tree

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

# DecisionTreeClassifier : 1. Represent 2. Evaluate = MODEL
clf = tree.DecisionTreeClassifier()

# Process Data
# fit function will do processing on data: i.e. Training of MODEL
# Supervised Learning
clf.fit(data, labels)

# Predictions
# input = [[1150, 1220]]
input = [[350, 350]]
output = clf.predict(input)
# print(output)

if output[0] == 0:
    print("Its a Bike")
else:
    print("Its a Car")
