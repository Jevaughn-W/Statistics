#This piece of the of code is to practice using APIs and obtaining datasets

import requests

response = requests.get("https://www.casact.org/")

print("hello world")
print(response.text)