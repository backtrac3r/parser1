import requests
from bs4 import BeautifulSoup as BS

headers = {
    # 'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}

params = {
    'v': 'KmzvSo90Zj4',
}

response = requests.get('https://www.youtube.com/watch', params=params, headers=headers)

html = BS(response.content, 'html.parser')

title = html.select("title")

print(title)
