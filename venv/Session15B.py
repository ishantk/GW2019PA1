def squareOfNumber(num=1):
    return num * num

lRef = lambda num=1 : num * num

numbers = [11, 12, 15, 19, 21]

# result = map(squareOfNumber, numbers)
result = map(lRef, numbers)
print(list(result))


L1 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lm1 = lambda n : n%2!=0
# result = map(lm1, L1)
result = filter(lm1, L1)
print(list(result))

X = [10, 20, 30, 40 ,50, 60]
Y = [11, 22, 33, 44 ,55]

print()

lm2 = lambda P, Q : P+Q
result = map(lm2, X, Y)
print(list(result))

punjabPopulation = [12151, 234121, 564223, 763441, 54542]

from functools import reduce

result = reduce(lm2, punjabPopulation)
print("Total Population is:",result)

# Explore the same with other Sequences :)

employees = [

    {"eid":101, "name":"John", "salary":10000},
    {"eid":201, "name":"Fionna", "salary":20000},
    {"eid":301, "name":"Jennie", "salary":30000}

]

lm3 = lambda emps : emps["name"]
result = map(lm3, employees)
print(list(result))



