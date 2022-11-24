import requests

url = "https://api.chucknorris.io/jokes/random"

params = {
    "LimiTo": "[nerdy]"
    }

response = requests.get(url, params)

joke = response.json()

print(joke)

