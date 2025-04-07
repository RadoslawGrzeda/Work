from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://desktop.pingone.eu/auchan-prod/Selection?cmd=selection")
time.sleep(2)

driver.find_element(By.ID, "identifierInput").send_keys("pol0014582")
time.sleep(2)
driver.find_element(By.ID, "postButton").click()
time.sleep(2)
driver.find_element(By.ID,"password").send_keys("")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "a.ping-button.normal.allow").click()
time.sleep(5)
driver.find_element(
    By.XPATH,
    "//span[@title='Salesforce Marketing Cloud']/ancestor::a"
).click()
time.sleep(5)

driver.find_element(
    By.ID,
        "otp"
).send_keys('123456')






wait = WebDriverWait(driver, 20)  # max 20 sekund
otp_input = wait.until(EC.presence_of_element_located((By.ID, "otp")))

otp_input.send_keys("1111")
time.sleep(2)
