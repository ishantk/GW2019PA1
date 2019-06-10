def fun(*args, **kwargs):
    print(args)
    print(kwargs)

fun(10, 20, 30, a=10, b=20, c=30)