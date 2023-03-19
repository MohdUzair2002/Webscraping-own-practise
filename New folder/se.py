##from selenium import webdriver
##from selenium.webdriver.chrome.service import Service
##from webdriver_manager.chrome import ChromeDriverManager
##from selenium.webdriver.chrome.options import Options
##from selenium.webdriver.support.ui import WebDriverWait
##from selenium.webdriver.common.by import By
##from selenium.webdriver.support import expected_conditions as EC
##import time
##
##
##options = Options()
##options.headless = True
##driver = webdriver.Chrome(r"G:\WEb SCrapping g\New folder\New folder/chromedriver.exe", options=options)
####s=Service(ChromeDriverManager().install())
####driver = webdriver.Chrome(service=s)
##driver.maximize_window()
##driver.get("https://www.fuel.com.gr/")
##time.sleep(5)
##T=driver.find_elements(By.id,"header-top-block") ##//div[@id='header-top-block']/a/text()
##print(T)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-data-dir=C:/Users/Mohammad Uzair/AppData/Local/Google/Chrome/User Data")
options.add_argument("--start-maximized")
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
sku=["L18P301002-BLK","DH8952-010"]
i=0
while (i<2):
    driver.maximize_window()
    driver.get("https://www.fuel.com.gr/")
    ##time.sleep(15)
    ##T=driver.find_element(By.XPATH,"//div[@id='header-top-block']/a").text
    ##element=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "btn-cookie-allow"))).click()

    element=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "open-elastic")))
    driver.execute_script("arguments[0].click();", element)


    ### time.sleep(5)
    ##print (T)
    ##element = WebDriverWait(driver, 10).until(
    ##            lambda driver : driver.find_element(By.ID,"//div[@class='header content']/button")
    ##    )   
    ##element.click()
    search=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "search")))
    search.clear()
    search.send_keys(sku[i])
    link=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@rel='noreferrer'][1]")))
    driver.execute_script("arguments[0].click();", link)
    size=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div[2]/div/div[2]/div[3]/form/div[1]/div/div/div/div/div[1]")))
    driver.execute_script("arguments[0].click();", size)
    cart=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "product-addtocart-button")))
    driver.execute_script("arguments[0].click();", cart)
    time.sleep(3)
    ##cart1=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/header/div/div/div[2]/div[2]/a")))
    ##driver.execute_script("arguments[0].click();", cart1)
    ##time.sleep(4)
    cart2=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "top-cart-btn-checkout")))
    driver.execute_script("arguments[0].click();", cart2)
    ##email=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'customer-email')))
    ##email.clear()
    ##email.send_keys("mohammad.uzair361@gmail.com")
    ##f_name=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div[2]/div/div[3]/div[4]/ol/li[1]/div[2]/form[2]/div/div[1]/div/input')))
    ##f_name.clear()
    ##f_name.send_keys("Mohammad ")
    ##l_name=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div[2]/div/div[3]/div[4]/ol/li[1]/div[2]/form[2]/div/div[2]/div/input
    ##')))
    ##l_name.clear()
    ##l_name.send_keys("Uzair ")
    ##add=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div[2]/div/div[3]/div[4]/ol/li[1]/div[2]/form[2]/div/fieldset/div/div/div/input')))
    ##add.clear()
    ##add.send_keys("flt 212 ")
    ##/html/body/div[2]/main/div[2]/div/div[3]/div[4]/ol/li[1]/div[2]/form[2]/div/div[3]/div/input
    ##city=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div[2]/div/div[3]/div[4]/ol/li[1]/div[2]/form[2]/div/div[3]/div/input')))
    ##city.clear()
    ##city.send_keys("khi ")
    ##/html/body/div[2]/main/div[2]/div/div[3]/div[4]/ol/li[1]/div[2]/form[2]/div/div[4]/div/input
    ##p_code=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div[2]/div/div[3]/div[4]/ol/li[1]/div[2]/form[2]/div/div[3]/div/input')))
    ##p_code.clear()
    ##p_code.send_keys("khi ")
    next1=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button action continue primary']")))
    driver.execute_script("arguments[0].click();", next1)
    cash=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/main/div[2]/div/div[3]/div[4]/ol/li[3]/div/form/fieldset/div[1]/div/div/div[5]/div[1]/label")))
    driver.execute_script("arguments[0].click();", cash)
##    buy=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/main/div[2]/div/div[3]/div[4]/ol/li[3]/div/form/fieldset/div[1]/div/div/div[5]/div[2]/div[5]/div/button")))
##    driver.execute_script("arguments[0].click();", buy)
    i+=1
