from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(30)
url = 'https://youtini.com/list/publishing-order'
wait = WebDriverWait(driver, 10)
driver.delete_all_cookies()
driver.get(url)
time.sleep(10)
get_url = driver.current_url
# wait.until(EC.visibility_of_all_elements_located())

titles = []

# if get_url == url:
#     page_source = driver.page_source

items = driver.find_elements(By.CLASS_NAME, 'text-block-181-copy')

count = 0
for item in items:
    try:
        titles.append(item.text)
    except:
        titles.append('No text')
        count += 1

print(len(items), count)
print(titles)


# soup = BeautifulSoup(page_source, features='html.parser')

# canon_break = soup.find(id='Age-of-Rebellion')

# lists = canon_break.find_all_next('div', class_='ro-collection-list-wrapper')

# for l in lists:
#     books = l.find_all('div', class_='w-dyn-item')
#     print(len(books))
