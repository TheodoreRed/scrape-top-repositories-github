import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("start-maximized")

webdriver_service = Service()
driver = webdriver.Chrome(options=options, service=webdriver_service)
wait = WebDriverWait(driver, 20)


url = "https://github.com/topics"
driver.get(url)


def click_load_more():
    load_more = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Load more')]"))
    )
    load_more.location_once_scrolled_into_view
    time.sleep(1)
    load_more.click()


click_load_more()
click_load_more()
click_load_more()
click_load_more()
click_load_more()


time.sleep(5)
html = driver.page_source
print(html)
with open("topics_html_source.html", "w", encoding="utf-8") as f:
    f.write(html)
