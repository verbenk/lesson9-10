import urllib.request
opener = urllib.request.build_opener()
responce = opener.open('https://uk.wikipedia.org/')
print(responce.read())
print('vedmedi valinuvedmedi valinuvedmedi valinuvedmedi valinuvedmedi valinuvedmedi valinu')

import requests
response = requests.get('https://uk.wikipedia.org/')
print(type(responce.content))