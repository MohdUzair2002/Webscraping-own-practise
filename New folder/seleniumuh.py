from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://www.psychologytoday.com/us/therapists/california?sid=6268171cd22b4&page=200")
link=driver.find_element(By.CLASS_NAME,"results-row-image")
                         
print(link.text)
##time.sleep(5)
##email=driver.find_element(By.ID,"email")
##email.clear()
##email.send_keys("hamadsaqib2@gmail.com")
##password=driver.find_element(By.ID,"pass")
##password.clear()
##password.send_keys("sgdfhfghfghfggj")
##T=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[3]/a").text
##print (T)
##Button=driver.find_element(By.CSS_SELECTOR,"button[name='login']")
##Button.click()
##time.sleep(5)
# s=Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()
# driver.get("https://www.fuel.com.gr/")
# time.sleep(5)
##T=driver.find_elements(By.CSS_SELECTOR,"div[role='heading']")
# T = WebDriverWait(driver,100).until(EC.presence_of_element_located(
#  (By.XPath, "tabla_evolucion")))

####print(T)
# ##from pyvirtualdisplay import Display
# ##
# ##display = Display(visible=0, size=(800, 800))  
# ##display.start()
# ##
# ##options = webdriver.ChromeOptions()
# ##options.add_argument('--no-sandbox')
# ##options.add_argument('start-maximized')
# ##options.add_argument('enable-automation')
# ##options.add_argument('--disable-infobars')
# ##options.add_argument('--disable-dev-shm-usage')
# ##options.add_argument('--disable-browser-side-navigation')
# ##options.add_argument("--remote-debugging-port=9222")
# ### options.add_argument("--headless")
# ##options.add_argument('--disable-gpu')
# ##options.add_argument("--log-level=3")
# ##driver = webdriver.Chrome(chromepath=r"G:\WEb SCrapping g\New folder\New folder/chromedriver.exe", chrome_options=options)
# ##url="https://www.fuel.com.gr/"
# ##
# ##driver.get(url)
# ##time.sleep(6)
# ##
# ##
# ##
# ##
# ##print(T)
# from selenium import webdriver
# from time import sleep
# import http.cookiejar
# import requests
# StringPROXY = "localhost:8080";

# org.openqa.selenium.Proxyproxy = neworg.openqa.selenium.Proxy();
# proxy.setHttpProxy(PROXY)
# proxy.setFtpProxy(PROXY)
# proxy.setSslProxy(PROXY);
# DesiredCapabilitiescap = newDesiredCapabilities();
# cap.setCapability(CapabilityType.PROXY, proxy);

# WebDriverdriver = newInternetExplorerDriver(cap);

# print ('Launching Firefox..')
# browser = webdriver.Chrome()
# print ('Entering to skidpaste.org...')
# browser.get('https://www.fuel.com.gr/')
# print ('Waiting 10 seconds...')
# sleep(10)
# a = browser.get_cookies()
# print ('Got cloudflare cookies:\n')
# print ('Closing Firefox..')
# browser.close()

# h = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0'}

# b = cookielib.CookieJar()

# for i in a:
#   ck = cookielib.Cookie(name=i['name'], value=i['value'], domain=i['domain'], path=i['path'], secure=i['secure'], rest=False, version=0,port=None,port_specified=False,domain_specified=False,domain_initial_dot=False,path_specified=True,expires=i['expiry'],discard=True,comment=None,comment_url=None,rfc2109=False)
#   b.set_cookie(ck)

# r = requests.get('https://www.fuel.com.gr/', cookies=b, headers=h)
# print (len(r.content))
# print (r.status_code)
