from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from twisted.application.strports import service

gecko_path = r"C:/Users/ASUS/Mã nguồn mở trong KHDL/pythonProject/geckodriver.exe"


ser = Service(gecko_path)



#tao tuy chon
options = webdriver.firefox.options.Options()

options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"

# thiet lap firefox chi hien thi giao dien
options.headless = False
#khoi tao driver
driver = webdriver.Firefox(options = options, service=ser)



#tao ulr
ulr = "http://pythonscraping.com/pages/javascript/ajaxDemo.html"
#truy cap

driver.get(ulr)
#in ra nd cua trang
print(driver.page_source)

time.sleep(3)

#In lai
print(driver.page_source)
driver.quit()