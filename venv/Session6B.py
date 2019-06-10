# Whatever we write in a Python file is executed automatically line by line
# Automatic : main thread in the process
# print(__name__)

def main(): # main can be any name
    print("Hello")
    print("This is a Good Day !!")

if __name__ == "__main__":
    main()