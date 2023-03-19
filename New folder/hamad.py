from optparse import TitledHelpFormatter
import requests
from bs4 import BeautifulSoup

url='https://en.wikipedia.org/wiki/Karachi'
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
Titledata=soup.find(id="firstHeading")
title=Titledata.text
paragraphs=soup.findAll('p')
for paragraph in paragraphs:
   para=paragraph.text
   attributes=paragraph.findAll('a')
   for attribute in attributes:
      link=attribute['href']
      print(link)

   # links=a['href']
   print(para)
   # print(a)



 
 