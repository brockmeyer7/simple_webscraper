from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://youtini.com/list/publishing-order'
driver.delete_all_cookies()
driver.get(url)
time.sleep(10)
get_url = driver.current_url

eras = []

results = driver.find_elements(
    By.CLASS_NAME, 'order-grid')

for item in results:
    eras.append(item.get_attribute('innerHTML'))

for e in eras[3:]:
    soup = BeautifulSoup(e, features='html.parser')
