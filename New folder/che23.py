from bs4 import BeautifulSoup
import requests
api_key='855808198d041ffb768e9b10e445c276'
Data='Mumbai'
url= 'http://api.openweathermap.org/data/2.5/weather?q=Mumbai&appid=855808198d041ffb768e9b10e445c276&units=metric'
response=requests.get(url)
print(response.status_code)  
print(response.json())
