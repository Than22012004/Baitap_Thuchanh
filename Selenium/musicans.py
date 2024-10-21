import string
import re
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import sqlite3

#cau hinh chrom de chay nen
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


#Tao DataFrame rong
d = pd.DataFrame({'band_name': [], 'years_active': []})


# Ham lay tt tung hoa si
def get_musicans_info(link):
    try:
        # Khoi tao webdriver
        driver = webdriver.Chrome(options=chrome_options)

        # mo trang
        driver.get(link)

        # Doi trang tai va dam bao the <h1> (ten ban nhac) xuat hien
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

        # Lay ten ban nhac
        try:
            name = driver.find_element(By.TAG_NAME, "h1").text
        except:
            name = ""

        # Lấy năm hoạt động
        try:
            years_active_element = driver.find_element(By.XPATH,
                                                       '//span[contains(text(),"Years active")]/parent::*/following-sibling::td').text
            years_active = years_active_element.text
        except:
            years_active = ""



        # Tao dictionary chua tt ban nhac
        musicians = {'band_name': name, 'years_active': years_active_element}

        return musicians

    except Exception as e:
        print(f"Lỗi khi truy cập {link}: {e}")
        return None

    finally:
        driver.quit()


def get_musician_links():
    driver = webdriver.Chrome(options=chrome_options)
    url = "https://en.wikipedia.org/wiki/Lists_of_musicians"

    links = []  # Khởi tạo danh sách lưu các liên kết nhạc sĩ

    try:
        driver.get(url)


        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "a")))
        list_links = driver.find_elements(By.XPATH, "//a[contains(text(), 'List of')]")

        if list_links:
            print("Danh sách các đường link bắt đầu bằng 'List of':")
            for link in list_links:
                href = link.get_attribute('href')
                print(href)  # Print each link

            # Truy cập vào liên kết đầu tiên trong danh sách
            first_link = list_links[0].get_attribute('href')
            driver.get(first_link)

            # Đợi trang tải và kiểm tra số lượng thẻ <ul>
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "ul")))

            # Lấy tất cả các thẻ <ul>
            ul_tags = driver.find_elements(By.TAG_NAME, "ul")
            max_li_count = 0
            ul_musician = None

            # Tìm thẻ <ul> có nhiều <li> nhất
            for ul in ul_tags:
                li_tags = ul.find_elements(By.TAG_NAME, "li")
                if len(li_tags) > max_li_count:
                    max_li_count = len(li_tags)
                    ul_musician = ul

            if ul_musician:
                # Lấy tất cả các liên kết nhạc sĩ
                li_tags = ul_musician.find_elements(By.TAG_NAME, "li")
                for li in li_tags:
                    try:
                        a_tag = li.find_element(By.TAG_NAME, "a")
                        link = a_tag.get_attribute("href")
                        if "/wiki/" in link:  # Chỉ lấy các liên kết đến Wikipedia
                            links.append(link)
                    except Exception as e:
                        print(f"Không tìm thấy liên kết: {e}")

            # In ra số lượng liên kết nhạc sĩ tìm thấy
            print(f"Tổng số liên kết nhạc sĩ tìm thấy: {len(links)}")
        else:
            print("Không tìm thấy liên kết nào bắt đầu bằng 'List of'.")
    except Exception as e:
        print(f"Error accessing musician list: {e}")
    finally:
        driver.quit()

    return links  # Trả về danh sách các liên kết nhạc sĩ





# su dung ThreadPoolExecutorde thu thap thong tin song song
#for letter in string.ascii_uppercase:  # Duyệt qua các chữ cái từ A đến Z
    #print(f"Đang xử lý các họa sĩ bắt đầu với '{letter}'")
musician_links = get_musician_links()
print(f"Thu thập được {len(musician_links)} ")

# su dung ThreadPoolExecutorde xu li cac thong tin song song
with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(get_musicans_info, musician_links))

# them ket qua vao DataFrame
for musicians in results:
    if musicians:
        d = pd.concat([d, pd.DataFrame([musicians])], ignore_index=True)

file_name = 'musicians.xlsx'
d.to_excel(file_name, index=False)
print('DataFrame đã được ghi vào file Excel thành công!!!!.')
