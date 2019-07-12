# Implementing NOT Operation with Perceptron
theta = -0.5

def activation(s):  # Binary Unit Step :)
    if s >= theta:
        return 1
    else:
        return 0

def summation(x, w):
    s = x * w
    y = activation(s)
    return y

input = 0
weight = -1

output = summation(input, weight)
print("For",input,"output is:",output)