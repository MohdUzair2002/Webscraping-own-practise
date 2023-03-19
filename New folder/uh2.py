import requests
from bs4 import BeautifulSoup
import csv
try:
    url='https://quotes.toscrape.com/'
    with open('QuotesToScrapeData.csv', 'w', newline='', encoding='UTF8') as csvfile:
        fieldnames = ['Title', 'Author', 'Author URL',"Tags","TagsURLS"]
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        while True:
            page=requests.get(url)
            soup=BeautifulSoup(page.content,'html.parser')
            quotes=soup.findAll("div",{"class":"quote"})
            for quote in quotes:
                Title=quote.find("span",{"class":"text"}).text
                Author=quote.find("small",{"class":"author"}).text
                try:
                    AuthorURL=quote.findAll("span")[1].find("a")["href"]
                except:
                    AuthorURL=""
                Tags=quote.find("div",{"class":"tags"}).findAll("a")
                TagText=[]
                TagURLS=[]
                for tag in Tags:
                    Tag=tag.text
                    TagURL=tag["href"]
                    print()
                    TagText.append(Tag)
                    TagURLS.append(TagURL)
                writer.writerow([Title,Author,AuthorURL,' ,'.join(TagText),';'.join(TagURLS)])
                print(f"Title:{Title}\nAuthor:{Author} URL={AuthorURL}\n Tags={' ,'.join(TagText)}\n TagsURL:{';'.join(TagURLS)}")
            Next=soup.find("li",{"class":"next"})
            if Next != None:
                url="https://quotes.toscrape.com/"+Next.find("a")["href"]
            else:
                break
except Exception as E:
    print("Error!! Please Try Again or Contact Your Developer...")