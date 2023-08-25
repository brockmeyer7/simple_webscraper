from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://youtini.com/list/publishing-order'
driver.delete_all_cookies()
driver.get(url)
time.sleep(10)
get_url = driver.current_url

eras = []
data = []

results = driver.find_elements(
    By.CLASS_NAME, 'order-grid')

for item in results:
    eras.append(item.get_attribute('innerHTML'))

for e in eras[3:]:
    soup = BeautifulSoup(e, features='html.parser')
    books = soup.find_all('div', 'w-dyn-item')
    for b in books:
        title = b.find('div', class_='text-block-181-copy').text
        author = b.find(
            'div', class_='rs-author-wrapper').find_all('div')[1].text
        published = b.find('div', class_='ro-date').find_all('div')[1].text
        type = b.find('div', class_='text-block-178-copy').text
        series = b.find('div', class_='series-wrapper-timeline').find('a').text
        img_src = b.find('a').find('img').attrs['src']
        if series not in ['Canon Movie Novelizations', '', 'Solo: A Star Wars Story Series', 'Clone Wars Animated Show Adaptations', 'Solo: A Star Wars Story Series'] and title != 'Rogue One':
            data.append([title, author, published, series, type, img_src])

data.sort(key=lambda x: (x[4], x[3]))

with open('canon_novels.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['Title', 'Author', 'Publication Date',
                    'Series', 'Novel Type', 'Image URL'])
    writer.writerows(data)
