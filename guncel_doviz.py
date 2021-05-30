import requests


url = "http://data.fixer.io/api/latest?access_key=2d632ede4abe8f05771bfb00c62d2cd4&format=1"


miktar =  float(input("Miktar"))


response = requests.get(url)


veri =  response.json()

#print(dir(response.json))

for i,j in veri["rates"].items():
    print(i,j)
