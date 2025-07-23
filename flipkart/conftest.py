import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from pageObjects.Browsepage import BrowsePage

driver = None

@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.use_chromium = True

    service = EdgeService(executable_path="D:/edgedriver_win64/msedgedriver.exe")
    driver = webdriver.Edge(service=service, options=options)
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.quit()