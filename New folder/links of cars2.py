from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import csv
with open('Links of cars', 'w', newline='', encoding='UTF8') as csvfile:
        fieldnames =["CarsURLS"]
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        s=Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
        driver.get("https://www.nettiauto.com/audi/100")
        T=driver.find_elements(By.CLASS_NAME,"tricky_link")
        for i in T:
          Links=i.get_attribute("href")
          print(Links)
          writer.writerow([Links])

        print(len(T))
