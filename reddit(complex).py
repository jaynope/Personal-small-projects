from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')

# website url
driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()), options=options)
driver.get("https://www.reddit.com/r/wallstreetbets/?f=flair_name%3A%22Daily%20Discussion%22")
time.sleep(5)

# click the most updated one

elem = driver.find_element_by_css_selector(
    "#t3_uyuv19 > div._1poyrkZ7g36PawDueRza-J._11R7M_VOgKO1RJyRSRErT3 > div._2FCtq-QzlfuN-SwVMUZMM3._3wiKjmhpIpoTE2r5KCm2o6.t3_uyuv19")
elem.click()
driver.maximize_window()
time.sleep(5)

# loop all the comments out
i = 0
for i in range(1400):
    try:
        print(f"loop {i}")
        target1 = driver.find_elements_by_css_selector("._3sf33-9rVAO_v4y0pIW_CH")[-4]
        target1.location_once_scrolled_into_view
        click1 = driver.find_element_by_css_selector("#moreComments-t1_ia88c8z , #moreComments-t1_ia8ehhj , #moreComments-t1_ia750cq > div._3_mqV5-KnILOxl1TvgYtCk > p")
        click1.click()
        time.sleep(3)
    except:
        pass
# loop the text
records = []
cells = driver.find_elements_by_css_selector("._3sf33-9rVAO_v4y0pIW_CH")
for j in cells:
    try:
        comments = j.find_element_by_css_selector("._1qeIAgB0cPwnLhDF9XSiJM")
        records.append([comments.text])
    except:
        pass

records[-1]
#notes : 100 loop around loop 1000 comments