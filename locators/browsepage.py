from selenium.webdriver.common.by import By


class Browsepage:
    close_btn = (By.XPATH, "//button[contains(text(), '✕')]")
    search_box = (By.NAME, "q")
    buy = (By.XPATH, "//button[contains(text(),'Buy Now')]")
    cart = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    item = (By.XPATH, "//div[@class='KzDlHZ']")
    color_white = (By.XPATH, "//div[@class='_0QyAeO')]")
    storage_128GB = (By.XPATH, "//a[contains(text(), '128 GB')]")
    storage_256GB = (By.XPATH, "//a[contains(text(), '256 GB')]")
    storage_512GB = (By.XPATH, "//a[contains(text(), '512 GB')]")
    submit = (By.XPATH, "//button[@id='submit']")
    error = (By.XPATH, "//div[@id='error']")
    success = (By.XPATH, "//h1[@class='post-title']")
    order = (By.XPATH, "//span[contains(text(), 'Place Order')]")

