import urllib.request
import json

url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'

def response(url):
    with urllib.request.urlopen(url) as response:
        return response.read()

res = response(url)
print(json.loads(res))
