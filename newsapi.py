import requests
import secrets

NEWSAPI_KEY = '0b3cda6a416d483481b3a07533465722'
base_url = 'https://newsapi.org/v2/top-headlines'
params = {
    "q": "new hampshire",
    "apiKey": secrets.NEWSAPI_KEY
}

response = requests.get(base_url, params)
result = response.json()
articles = result["articles"]
for a in articles:
    print(a["title"], "-", a["source"]["name"])