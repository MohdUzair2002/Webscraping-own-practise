##import requests
##from bs4 import BeautifulSoup
##url='https://uok.edu.pk/sfao/scholarships.php#y2021'
##page=requests.get(url)
##soup=BeautifulSoup(page.content,'html.parser')
##scho1=soup.find(class_='course_content')
##sc1=scho1.find_all('ul')[3]
##sc2=sc1.text.replace("::  Click here","")
####for sc1 in scho1:
##print((sc2))
##sc3=sc1.find_all('li')
##for i in sc3:
##    sc4=i.find('a')['href']
##    print('https://uok.edu.pk'+sc4)
import requests
from bs4 import BeautifulSoup
url='https://uok.edu.pk/sfao/scholarships.php#y2021'
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
scho1=soup.find(class_='course_content')
sc1=scho1.find_all('ul')
for i in sc1:
    sc2=i.findAll("li")
    for j in sc2:
        try:
            print(j["href"])
        except:
            pass
