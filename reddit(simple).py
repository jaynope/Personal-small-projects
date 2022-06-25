from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')

#website url
driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()), options=options)
driver.get("https://www.reddit.com/r/wallstreetbets/comments/uzbuxt/federal_reserve_wants_lower_wages/")
driver.maximize_window()
time.sleep(3)

#loop all the comments out
i = 0
for i in range(50):
    try:
        print(f"loop {i}")
        target = driver.find_elements_by_css_selector("._3tw__eCCe7j-epNCKGXUKk")[-4]
        target.location_once_scrolled_into_view
        elem = driver.find_element_by_css_selector("#moreComments-t1_ia9w9af , #moreComments-t1_iacg7wg > div._3_mqV5-KnILOxl1TvgYtCk > p")
        elem.click()
        time.sleep(3)
    except:
        pass

#loop the text

records = []
cells = driver. find_elements_by_css_selector("._3sf33-9rVAO_v4y0pIW_CH")
for i in cells:
    try:
        comments = i.find_element_by_css_selector("._1qeIAgB0cPwnLhDF9XSiJM")
        records.append([comments.text])
    except:
        pass


records [-1]







