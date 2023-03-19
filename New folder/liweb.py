

















from bs4 import BeautifulSoup
import requests
url="https://www.americanas.com.br/busca/maos?rc=maos"
Page=requests.get(url)
print(Page.status_code)








##from selenium import webdriver
##from selenium.webdriver.chrome.service import Service
##from webdriver_manager.chrome import ChromeDriverManager
##from selenium.webdriver.chrome.options import Options
##from selenium.webdriver.support.ui import WebDriverWait
##from selenium.webdriver.common.by import By
##from selenium.webdriver.support import expected_conditions as EC
##import time
##from bs4 import BeautifulSoup
##import csv
##with open('Links of cars', 'w', newline='', encoding='UTF8') as csvfile:
##        fieldnames =["CarsURLS"]
##        writer = csv.writer(csvfile)
##        writer.writerow(fieldnames)
##        s=Service(ChromeDriverManager().install())
##        driver = webdriver.Chrome(service=s)
##        driver.maximize_window()
##        driver.get("https://www.nettiauto.com/audi/100")
##        T=driver.find_elements(By.CLASS_NAME,"tricky_link")
##        for i in T:
##          Links=i.get_attribute("href")
##          print(Links)
##          writer.writerow([Links])
##
##        print(len(T))

##s=Service(ChromeDriverManager().install())
##driver = webdriver.Chrome(service=s)
##driver.maximize_window()
##driver.get("https://www.facebook.com/")
##time.sleep(5)
##email=driver.find_element(By.ID,"email")
##email.clear()
##email.send_keys("hamadsaqib2@gmail.com")
##password=driver.find_element(By.ID,"pass")
##password.clear()
##password.send_keys("sgdfhfghfghfggj")
##Button=driver.find_element(By.CSS_SELECTOR,"button[name='login']")
##Button.click()
##time.sleep(5)
##chrome_options = Options()
##chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8000")

##soup=BeautifulSoup(driver.page_source,"html.parser")
##Links=soup.find_all("a",{"class":"tricky_link"})
##for Link in Links:
##    print(Link["href"])











# from re import S
# import requests
# from requests_html import HTMLSession
# from bs4 import BeautifulSoup
# import csv

# url="https://www.nettiauto.com/audi/100"
# s = HTMLSession()
# page=s.get(url)
# print(page.status_code)
# page=soup=BeautifulSoup(page.html.html,'html.parser')
# quotes=soup.findAll("div",{"class":"tricky_link"})
# print (quotes)
