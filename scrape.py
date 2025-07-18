from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
# options.add_argument("--headless")
options.use_chromium = True

service = EdgeService(executable_path="D:/edgedriver_win64/msedgedriver.exe")

driver = webdriver.Edge(service=service, options=options)


try:
    driver.get("https://practicetestautomation.com/")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".elementor-post__title a")))

    titles = driver.find_elements(By.CSS_SELECTOR, ".elementor-post__title a")

    for t in titles:
        title_text = t.text  
        href = t.get_attribute("href")
        print(f"{title_text} → {href}")
finally:
    driver.quit()
