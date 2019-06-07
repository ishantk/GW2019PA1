# Built-Ins on Strings

# Strings are IMMUTABLE
# Whenever we perform any modification operation on String we get a new String in memory
name = "Fionna Flynn"
newName = name.upper()
print(name)
print(newName)

anotherName = "john watson"
anotherName = anotherName.capitalize()
print(anotherName)

names = "John, Jennie, Jim, Jack, John, Joe"
# idx = names.index("h")
idx = names.index("Jennie")
print(idx)

newNames = names.replace('J', 'K')
print(names)
print(newNames)

# Find Occurance of some substring
# num = names.count("J", 0, len(names))
num = names.count("John", 0, len(names))
print(num)

print()

data = names.split(",")
print(data, type(data))

print()

for n in data:
    print(n.strip())

quote = "Search the candle rather than cursing the darkness"
data = quote.split(" ")
print(data, len(data))

saluation = "Mr."
fname = "George"

name = saluation + fname
print(name)

number = "Hundred"
print(type(number))

if number.isdigit():
    n = int(number)
    print("n is:",n,type(n))

songName = "Hello.mp3"
if songName.endswith(".mp3"):   # startsWith
    print("Play the Audio File")

# Explore More String Built Ins by using your . as intellisense
