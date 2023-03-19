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
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-data-dir=C:/Users/Mohammad Uzair/AppData/Local/Google/Chrome/User Data")
options.add_argument("--start-maximized")
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
driver.maximize_window()
driver.get("https://www.fuel.com.gr/")
time.sleep(15)
T=driver.find_element(By.XPATH,"//div[@id='header-top-block']/a")
#  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='header content']/button"))).click()
# time.sleep(5)
print (T)
element = WebDriverWait(driver, 10).until(
            lambda driver : driver.find_element(By.XPATH,"//div[@class='header content']/button")
    )   
element.click()
# search=driver.find_element(By.XPATH,"//div[@class='the-input-area']/input")
# search.clear()
# search.send_keys("VN0A5KMF3KS1")

