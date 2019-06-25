import re

# https://www.vogella.com/tutorials/JavaRegularExpressions/article.html
quote = "Search the Candle Rather than cursing the Darkness"
# result = re.match("Search", quote) # match from starting
# result = re.match("Candle", quote)
# result = re.search("the", quote)
result = re.findall("the", quote)
print(result)
print(type(result))

print()

# data = re.split("the", quote)
# print(data)

data = re.sub("the", "a", quote)
print(quote)
print(data)


