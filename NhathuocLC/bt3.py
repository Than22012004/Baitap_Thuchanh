from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import pandas as pd
from selenium import ActionChains
from shoppe import driver

# Đường dẫn đến file thực thi geckodriver
gecko_path = r"C:/Users/ASUS/Mã nguồn mở trong KHDL/pythonProject/geckodriver.exe"


# Khởi tởi đối tượng dịch vụ với đường geckodriver
ser = Service(gecko_path)

# Tạo tùy chọn
options = webdriver.firefox.options.Options();
options.binary_location ="C:/Program Files/Mozilla Firefox/firefox.exe"
# Thiết lập firefox chỉ hiện thị giao diện
options.headless = False


# Tạo url
ulr = 'https://pythonscraping.com/pages/files/form.html'
# Truy cập
driver.get(ulr)


firstname_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
lasttname_name = driver.find_element(By.XPATH, "//input[@name='lasttname']")



fristname_input.send_keys('Van Than')
time,sleep(1)

lastname_input.send_keys('Pham')


button = driver.find_element((By.XPATH, "//input[@type='submit']"))
button.click()
time.sleep(5)