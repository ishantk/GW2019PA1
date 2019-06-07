quote = "Work Hard Be Luckier"
# data = list(quote)
# data = tuple(quote)
# data = set(quote)
# data = dict(quote) -> Try to explore this !!
# print(data)

print(quote * 2)
print(quote[::-1])

# for i in range(0, len(quote)):
for i in range(len(quote)-1, -1, -1):
    print(quote[i], end=" ")
