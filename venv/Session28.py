"""
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


from sklearn.naive_bayes import GaussianNB

# 1. Create the DataSet | Supervised Learning
FEATURES = [ [100, 100],
         [150, 110],
         [180, 150],
         [200, 180],
         [800, 1000],
         [1000, 1200],
         [1200, 1300],
         [1500, 1500]
       ]

LABELS = [0, 0, 0, 0, 1, 1, 1, 1]

NAMES = ["Bike", "Car"]

# 2. Create the Model
model = GaussianNB()

# 3. Train the Model
model.fit(FEATURES, LABELS)

sampleInput = [190, 175]

predictedClass = model.predict([sampleInput])

print(">> Predicted Class is:",predictedClass)
print(">> Predicted Class is:",predictedClass[0])
print(">> Predicted Class is:",NAMES[predictedClass[0]])