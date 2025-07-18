from selenium.webdriver.common.by import By


class Homepage:
    user =(By.XPATH, "//input[@id='username']")
    password = (By.XPATH, "//input[@id='password']")
    submit = (By.XPATH, "//button[@id='submit']")
    error = (By.XPATH, "//div[@id='error']")
    success = (By.XPATH, "//h1[@class='post-title']")

class Login:
    text = (By.XPATH, "//strong[contains(text(),'logged in')]")
    logout = (By.XPATH, "//a[.='Log out']")