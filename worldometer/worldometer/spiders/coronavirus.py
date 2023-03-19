from datetime import datetime
from dataclasses import replace
from os import link
from re import I
from turtle import title
from async_generator import yield_
from numpy import product
from pytest import Item
import scrapy
from scrapy.selector import Selector
import pandas as pd
from scraper_api import ScraperAPIClient

class CoronavirusSpider(scrapy.Spider):
    name = 'coronavirus'
    # allowed_domains = ['www.americanas.com.br']
    i=1
   
    start_urls = ['https://www.psychologytoday.com/us/therapists/california?sid=6268171cd22b4&page=200&fbclid=IwAR3DrsJJKIOYKMU195z_94CfMHTwOCAG77f5VSiUhtaxgO_9gPyCuJryQ1c']  
    def parse(self, response):
      links=response.xpath("//a[@class='results-row-image']")
      for link in links:
        FLink=link.xpath(".//@href").get()
      
        yield scrapy.Request(url=FLink,callback=self.GetData)
    def GetData(self,response):
     
        
        chec_web=response.xpath("//a[@class='btn btn-md btn-profile btn-default hidden-sm-down']/@href").get()
        if chec_web:
         spec=response.xpath("//li[@class='highlight'][1]/text()").get()
         f_name=response.xpath("//h1[@itemprop='name']/text()").get()
         
         yield scrapy.Request(url=chec_web, cb_kwargs=dict(main_url=spec,f_name=f_name),callback=self.dt)

        else:
          ff=0
          
    def dt(self,response,main_url,f_name):
      
          main_url=main_url
          f_name=f_name
          sf_nam1=f_name.split(' ')
       
          sf_nam=sf_nam1[0]
          l_sf_nam=sf_nam.lower()

          email=response.xpath("//*[contains(@href,'mailto:')]/@href").get()
          print(email)
          sp_em1=email.split('@')
          sp_em=sp_em1[0]
          l_sp_em=sp_em.lower()
         
          cmp_name=response.xpath("//meta[@property='og:title']/@content").get()
          cmp_name=cmp_name.lower()
          if l_sf_nam in cmp_name:
            cmp_name="Yours Company"
            
          if email:
              
           if l_sf_nam in l_sp_em:
             f_name=sf_nam
           else:
             f_name="there"
           
           yield{
            # "Countryname":name,
            # # "Countrylink":link
            # "price":price
           
            #  "website":  response ,
             "email":email[7:]  ,
             "Company Name":cmp_name,
             "Specification":main_url,
             'f1':f_name

              }
           yield dict 
           {
             'na':main_url,
           }
          else:
             hu="rf"
             fd="kk"
          t=str(CoronavirusSpider.i)
          next_page=f"https://www.psychologytoday.com/us/therapists/california?sid=6268171cd22b4&page={CoronavirusSpider.i}&fbclid=IwAR3DrsJJKIOYKMU195z_94CfMHTwOCAG77f5VSiUhtaxgO_9gPyCuJryQ1c"
      #     if int(SpidernameSpider.a )>24:
      #      if int(SpidernameSpider.a) <=9976:
          if CoronavirusSpider.i<=500:
             CoronavirusSpider.i+=1
             yield  response.follow(next_page,callback=self.parse)
          #    yield{
          #   # "Countryname":name,
          #   # # "Countrylink":link
          #   # "price":price
            
          #    "website": hu ,
          #    "email":fd  }
        
          # i=i+1
    
##      ULinks=links.xpath(".//a[@aria-current='page']")
        #  Selectors=response.xpath("(//h3[@class='product-name__Name-sc-1shovj0-0 gUjFDF'])")
        #  price=response.xpath("//span[@class='src__Text-sc-154pg0p-0 price__PromotionalPrice-sc-h6xgft-1 ctBJlj price-info__ListPriceWithMargin-sc-1xm1xzb-2 liXDNM']")

        #  for product,p in zip(Selectors,price):
##      print (len(ULinks))
##      for link in ULinks:
##          link=link.xpath(".//@href").get()
      # yield scrapy.Request(url=link,callback=self.parse)
          # name=product.xpath(".//text()").get()
          # price=p.xpath(".//text()").get()
       
     #   link=product.xpath("//div[@class='inStockCard__Wrapper-sc-1ngt5zo-0 iRvjrG']/a/@href").get()
      
### import scrapy
### from scrapy.selector import Selector
##
### class CoronavirusSpider(scrapy.Spider):
###     name = 'coronavirus'
###     allowed_domains = ['www.americanas.com.br']
###     start_urls = ['https://www.americanas.com.br/produto/4265732670?pfm_carac=computer&pfm_page=search&pfm_pos=grid&pfm_type=search_page&offerId=61827372d9fd6edeec2cd26f']
###     def parse(self, response):
###             seller=response.xpath("/html/body/div[1]/div/div/main/div[2]/div[2]/div[4]/p/a[1]/@href").get().split("/")[-1]
##
###             discription=response.xpath("/html/body/div[1]/div/div/main/div[2]/div[2]/div[4]/p/a[1]/text()").get()
##
###             #  for product,p in zip(seller,price):
###             #   name=product.xpath(".//text()").get()
###             #   price=p.xpath(".//text()").get()
###             #   link=product.xpath("//div[@class='inStockCard__Wrapper-sc-1ngt5zo-0 iRvjrG']/a/@href").get()
###             yield{
###                 "seller":seller,
###                 # "Countrylink":link
###                 "description":discription
###               }

##
##class CoronavirusSpider(scrapy.Spider):
##    name = 'coronavirus'
##    # allowed_domains = ['www.americanas.com.br']
##    start_urls = ['https://www.americanas.com.br/busca/maos']
##
##    def parse(self, response):
##      
##      links=response.xpath("/html/body/div[1]/div/div/main/div/div[3]/div[2]")
##      ULinks=links.xpath(".//a[@aria-current='page']")
##      for link in ULinks:
##          link=link.xpath(".//@href").get()
##          FLink=response.urljoin(link)
##         
##
##          yield scrapy.Request(url=FLink,callback=self.GetData)
##   
##    def GetData(self,response):
##         
##          items=WorldometerItem()
##          name1=response.xpath("/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/h1/text()").get()
##          discription=response.xpath("/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/div[3]/p/text()").get()
##          pricecurrency=response.xpath("/html/body/div[1]/div/div/main/div[2]/div[2]/div[1]/div[1]/div//text()").get()
##          url=response.url,
##          price1=response.xpath("(/html/body/div[1]/div/div/main/div[2]/div[2]/div[1]/div[1]/div//text())[2]").get()
##          price=pricecurrency+price1.replace(",",".")
##          productid=(response.url.split("/")[4]).split("?")[0]
##          sellerdetail=(response.xpath("/html/body/div[1]/div/div/main/div[2]/div[2]/div[4]/p/strong/font/font/text()")).get()
##          if sellerdetail  =="Americanas":
##           seller_name="Americanas"
##           sellerid="Americanas"
##          else:
##           seller_name=response.xpath("//*[@id='rsyswpsdk']/div/main/div[2]/div[2]/div[4]/p/a[1]//text()").get()
##           sellerid=response.xpath("/html/body/div[1]/div/div/main/div[2]/div[2]/div[4]/p/a[1]/@href").get().split("/")[-1]
##          image=response.xpath("/html/body/div[1]/div/div/main/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/picture/img/@src").get()
##          items['Title']=name1
##          items['Price']=price
##          items['Description']=discription
##          items['ProductID']=productid
##          items['Sellername']=seller_name
##          items['SellerID']=sellerid
##          items['URL']=url
##          items['Image']=image
##          yield items
##                # "title":name1,
##                # "price":pricecurrency+price.replace(",","."),
##                # "sellerid":sellerid,
##                # "seller name":seller_name,
##                # "description":discription,
##                # "image":image,
##                # "url":response.url,
##                # "
##                
##                 
                
            
          

    
