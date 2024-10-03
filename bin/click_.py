import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


urls = []
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

for p in range(11, 15):  # 15
    url = "https://history.colife.org.tw/#/?cd=%2F"
    driver.get(url)
    time.sleep(3)
    driver.find_elements(By.CSS_SELECTOR, "a.is-block.name")[2].click()
    time.sleep(2)

    driver.find_elements(By.CSS_SELECTOR, "a.is-block.name")[2].click()
    time.sleep(2)

    driver.find_elements(By.CSS_SELECTOR, "a.is-block.name")[p].click()
    time.sleep(2)

    elements = driver.find_elements(By.CSS_SELECTOR, "a.is-block.name")
    print(elements)

    for i in elements[1:]:
        i.click()
        time.sleep(1)
    time.sleep(5)

driver.quit()
