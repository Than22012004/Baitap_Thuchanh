from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import getpass
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Đường dẫn đến file thực thi geckodriver
gecko_path = r"C:/Users/ASUS/Mã nguồn mở trong KHDL/pythonProject/geckodriver.exe"

# Khởi tạo đối tượng dịch vụ với đường dẫn geckodriver
ser = Service(gecko_path)

# Tạo tùy chọn cho Firefox
from selenium.webdriver.firefox.options import Options
options = Options()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
options.headless = False  # Set to True if you want to run in headless mode

# Khởi tạo driver
driver = webdriver.Firefox(options=options, service=ser)

# URL for Reddit login
url = 'https://www.reddit.com/login/'
driver.get(url)
#time.sleep(3)

# Nhập thông tin đăng nhập
user_name = input('Please provide your email: ')

my_pass = getpass.getpass('Please provide your password: ')

# Đăng nhập
#username_input =driver.find_element(By.XPATH, "//input[@name='username']")
#password_input =driver.find_element(By.XPATH, "//input[@name='password']")

# Nhấn thông tin và nhấn nút Enter
#username_input.send_keys(my_email)
#password_input.send_keys(my_password + Keys.ENTER)
#time.sleep(5)


actionChains = ActionChains(driver)
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.send_keys(user_name).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()

actionChains.send_keys(my_pass+Keys.ENTER).perform()
#truy cap trang post bai

ulr2 = 'https://www.reddit.com/user/navnaht/submit/?type=TEXT'
driver.get(ulr2)
time.sleep(2)
for i in range(16):
    actionChains.key_down(Keys.TAB).perform()
    time.sleep(1)

actionChains.send_keys('Vi du post').perform()

actionChains.key_down(Keys.TAB).perform()
actionChains.send_keys('pvt' + Keys.ENTER).perform()

for i in range(4):
    actionChains.key_down(Keys.TAB).perform()
    time.sleep(1)

actionChains.key_down(Keys.ENTER).perform()

time.sleep(15)
driver.quit()