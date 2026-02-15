from backend.middlewares.APIdata import Settings
import requests

data = Settings()

def get_info_by_api():
    headers = {"X-Api-Key": data.API_KEY}
    r = requests.get(data.URL, headers=headers)
    g = r.json()
    print(
        f"Username: {g[0]["username"]}\nPassword: {g[0]["password"]}\nEmail: {g[0]["email"]}\n\
First Name: {g[0]["first_name"]}\nLast Name: {g[0]["last_name"]}\nFull Name: {g[0]["full_name"]}"
        )
    return r.json()