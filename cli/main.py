import requests
from cli.config import Data

data = Data()

headers = {"X-Api-Key": data.API_KEY}

r = requests.get(url=data.URL, headers=headers)

print(
    f"Username: {r.json()[0]["username"]}\nPassword: {r.json()[0]["password"]}\nEmail: {r.json()[0]["email"]}\n\
First Name: {r.json()[0]["first_name"]}\nLast Name: {r.json()[0]["last_name"]}\nFull Name: {r.json()[0]["full_name"]}"
    )