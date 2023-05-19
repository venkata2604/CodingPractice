import requests
from bs4 import BeautifulSoup
import scrapy

URL = 'https://quintewest.maps.arcgis.com/apps/webappviewer/index.html?id=6f9d5bae46044c9587c21cd8cf9b098f'


result = requests.get(URL)
print(result)

 