from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import time

options = Options()
options.use_chromium = True

service = EdgeService(executable_path="D:/edgedriver_win64/msedgedriver.exe")

driver = webdriver.Edge(service=service, options=options)

driver.get("https://practicetestautomation.com/practice-test-login/")

time.sleep(1)

driver.find_element(By.NAME, "username").send_keys("student")
driver.find_element(By.NAME, "password").send_keys("Password123"+ Keys.RETURN)
driver.find_element(By.ID, "submit").click()
# time.sleep(3)
# driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

time.sleep(2)
print("Login attempt complete.")
print("Current URL:", driver.current_url)

driver.quit()
