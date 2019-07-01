import requests
from bs4 import BeautifulSoup # External Library for Parsing HTML Data

url = "https://twitter.com/dna"
response = requests.get(url)
# print(response.text)

# HTML Parsing : From HTML Code extract the desired/meaningful information

soup = BeautifulSoup(response.text, "html.parser")
print("Type of Soup is:", type(soup))
print("********************")
# print(soup)
# print(soup.prettify())

print("Title is:",soup.title.text)
print("********************")

print()

# children = soup.children
# for child in children:
#     print(child)
#     print("----------------------")

# pTags = soup.find_all("p")
# for tag in pTags:
#     print(tag)
#     print("----------------------")

# divTags = soup.find_all("div")
divTags = soup.find_all("div", class_="js-tweet-text-container")
for tag in divTags:
    # print(tag)
    print(tag.text)
    print("----------------------")