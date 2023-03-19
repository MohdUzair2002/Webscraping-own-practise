import requests
from requests_html import HTMLSession
url="https://beta.quran.com/67"
s=HTMLSession()
r=s.get(url)
r.html.render(sleep=1)
path=r.html.xpath('//*[@id="__next"]/div/div[3]',first=True)
for item in path.absolute_links:
    r=s.get(item)
    print(r.html.find('div.QuranReader_container__8c0FU',first=True)).text
