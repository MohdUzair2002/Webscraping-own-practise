##import pandas as pd
##import warnings
##warnings.filterwarnings('ignore')
##from bs4 import BeautifulSoup
##from selenium import webdriver
##from selenium.common.exceptions import InvalidSessionIdException
##from selenium.common.exceptions import NoSuchElementException
##from selenium.webdriver.chrome.options import Options
##from selenium.webdriver.common.keys import Keys
##from selenium.webdriver.common.by import By
##from selenium.webdriver.support.ui import WebDriverWait
##from selenium.webdriver.support import expected_conditions as EC
##options = webdriver.ChromeOptions()
##options.add_argument("--disable-blink-features=AutomationControlled")
##options.add_argument('--ignore-certificate-errors-spki-list')
##options.add_argument('--ignore-ssl-errors')
##options.add_experimental_option('excludeSwitches', ['enable-logging'])
##options.add_argument('--headless')
##options.add_argument('--no-sandbox')
##options.add_argument('--disable-dev-shm-usage')
##driver = webdriver.Chrome(options=options, executable_path=r"G:\WEb SCrapping g\New folder\New folder/chromedriver")
##print("Current session is {}".format(driver.session_id))
##driver.maximize_window()
##driver.get("https://www.fuel.com.gr/is using Cloudflare CDN/Proxy!")
##html = BeautifulSoup(driver.page_source)
##innerContent = driver.find_elements(By.XPATH,"//div[@id='header-top-block']/a")
##print(innerContent)
##import cloudscraper
##from bs4 import BeautifulSoup
##scraper = cloudscraper.create_scraper(delay=10,   browser={'custom': 'ScraperBot/1.0',})
##url = "https://www.fuel.com.gr/"
##req= scraper.get(url)
###print(req)
##
##soup = BeautifulSoup(req.content, "html.parser")
##txt=soup.find('h1',class_="noticia titulo").text
##print(txt)
import cloudscraper

# create a cloudscraper instance
scraper = cloudscraper.create_scraper()

print (scraper.get("https://www.fuel.com.gr/").text)
