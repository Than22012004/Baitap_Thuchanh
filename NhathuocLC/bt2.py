from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import pandas as pd

# Đường dẫn đến file thực thi geckodriver
gecko_path = r"C:/Users/ASUS/Mã nguồn mở trong KHDL/pythonProject/geckodriver.exe"


# Khởi tởi đối tượng dịch vụ với đường geckodriver
ser = Service(gecko_path)

# Tạo tùy chọn
options = webdriver.firefox.options.Options();
options.binary_location ="C:/Program Files/Mozilla Firefox/firefox.exe"
# Thiết lập firefox chỉ hiện thị giao diện
options.headless = False

# Khởi tạo driver
driver = webdriver.Firefox(options = options, service=ser)

# Tạo url
ulr = 'https://nhathuoclongchau.com.vn/thuc-pham-chuc-nang/vitamin-khoang-chat/'
# Truy cập
driver.get(ulr)


# tim phan tu body ua trang de gui phim mui ten len xuong
body = driver.find_element(By.TAG_NAME, "body")
time.sleep(3)
for k in range(50):
    try:
        # Lấy tất cả các button trên trang
        buttons = driver.find_elements(By.TAG_NAME, "button")

        # Duyệt qua từng button
        for button in buttons:
            # Kiểm tra nếu nội dung của button chứa "Xem thêm" và "sản phẩm"
            if "Xem thêm" in button.text and "sản phẩm" in button.text:
                # Di chuyển tới button và click
                button.click()
                break  # Thoát khỏi vòng lặp nếu đã click thành công

    except Exception as e:
        print(f"Lỗi: {e}")

for i in range(50):
    body.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.01)
time.sleep(5)


#tao list
stt = []
tensp = []
gia = []
hinh_anh = []
# Tìm tất cả các button có nội dung là "Chọn mua"
buttons = driver.find_elements(By.XPATH, "//button[text()='Chọn mua']")

print(len(buttons))

# lay tung san pham
for i, bt in enumerate(buttons, 1):
    # Quay ngược 3 lần để tìm div cha
    parent_div = bt
    for _ in range(3):
        parent_div = parent_div.find_element(By.XPATH, "./..")  # Quay ngược 1 lần

    sp = parent_div

    # Lay ten sp
    try:
        tsp = sp.find_element(By.TAG_NAME, 'h3').text
    except:
        tsp = ''

    # Lat gia sp
    try:
        gsp = sp.find_element(By.CLASS_NAME, 'text-blue-5').text
    except:
        gsp = ''

    # Lat hinh anh
    try:
        ha = sp.find_element(By.TAG_NAME, 'img').get_attribute('src')
    except:
        ha = ''
    if len(tsp) > 0:
        stt.append(i)
        tensp.append(tsp)
        gia.append(gsp)
        hinh_anh.append(ha)

#tao dataframe
df = pd.DataFrame({
    "STT": stt,
    "Tên sản phẩm": tensp,
    "Giá bán": gia,
    "Hình ảnh": hinh_anh

})


df.to_excel('Ds_sanpham2.xlsx', index =False)
# Đóng browser
driver.quit()

