# Keyword Arguments
def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))

# fun(a=10, b=20, name="John")
# fun(10="John", 20="Jennie", 30="Hello") error
# Rule : Key must not be a number