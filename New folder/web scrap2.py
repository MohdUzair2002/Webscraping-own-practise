import requests
from bs4 import BeautifulSoup
url="https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm"
page=requests.get(url)
print(page.status_code)
soup=BeautifulSoup(page.content,'html.parser')
zcontent=soup.find(class_='BodyText')
zcontent1=zcontent.find_all('a')
last_links=soup.find(class_='AlphaNav')
last_links.decompose()
i=0
for names1 in (zcontent1):
    names=names1.contents[0]
    links='https://web.archive.org'+names1.get('href')
    print(names)
    print(links)
