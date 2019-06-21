def hello():
    return "Hello"

# Reference Copy
h = hello


print(h)            # HashCode
print(type(h))      # function

print(hello())
print(h())

print("*************")

def helloAgain():
    yield  "Hi"
    yield "Hello"
    yield "Heya"
    yield "Namaste"

# Reference Copy
ha = helloAgain
print(ha)           # HashCode
print(type(ha))     # function
print(ha())         # Execution of a function which is yielding returns Generator

gen = ha()
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


