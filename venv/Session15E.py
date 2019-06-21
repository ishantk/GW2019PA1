def hello():
    print("Hello..")

    # Nested Function or Local Function
    def bye():
        print("Bye..")

    print(bye)
    bye()

print(hello)
hello()