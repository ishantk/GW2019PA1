import os

print(os.getcwd())
print(os.name)
print(os.uname())
print(os.getlogin())
print(os.getppid())

pathToDir = "/Users/ishantkumar/Downloads"
pathToFile = "/Users/ishantkumar/Downloads/orders.csv"
print("Is Downloads available:", os.path.exists(pathToDir))
print("Is orders.csv available:", os.path.exists(pathToFile))

# path = "/Users/ishantkumar/Downloads/MyPythonPrograms"
# os.mkdir(path)

"""
print(os.getcwd())
os.chdir("/Users/ishantkumar/Downloads/MyPythonPrograms")
print(os.getcwd())
"""

# os.rmdir("/Users/ishantkumar/Downloads/MyPythonPrograms")
# print(">> Directory Removed")

files = os.walk("/Users/ishantkumar/Downloads")
print("files:",files)

allFiles = list(files)
for file in allFiles:
    print(file)

# Assignment
# Ask path of a folder from user as input
# Tell him how many number of audio files, video files and documents exists
# Explore : To find all those files which were created long ago and are not in use :)