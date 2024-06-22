import requests
from bs4 import BeautifulSoup as BS

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

params = {
    'v': 'KmzvSo90Zj4',
}

response = requests.get('https://www.youtube.com/watch', params=params, headers=headers)

html = BS(response.content, 'html.parser')

title = html.select("title")

print(title)
