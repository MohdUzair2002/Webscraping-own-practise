import bs4
import requests

url="https://www.youtube.com/channel/UCa5UDzFzpIjJ1VSxCSlQP_g"
data=requests.get(url)
soup=bs4.BeautifulSoup(data.text,'html.parser')
##print(soup.prettify())
##for para in soup.find_all('p'):
##    print(para.text)
for links in soup.find_all(class_='BodyText'):
    link=links.get('href')
    
   
##    if link[0:3]=="../" and link!='#':
##        print("https://www.youtube.com/channel/UCw3zWrRUDYFR3pfyrqQLeYQ"+link[2:len(link)])

    if link[0:3]=="/" :
        print("https://www.youtube.com/channel/UCw3zWrRUDYFR3pfyrqQLeYQ"+link)
    elif (link!='#'):
        print(link)
