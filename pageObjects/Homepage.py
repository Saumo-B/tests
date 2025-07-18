from locators.homepage import Homepage as home
from locators.homepage import Login as page
from utilities.Wait import Wait

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_user(self, user):
        box = Wait.clickable(self.driver, home.user)
        box.send_keys(user)

    def get_password(self, password):
        box = Wait.clickable(self.driver, home.password)
        box.send_keys(password)

    def click_submit(self):
        submit = Wait.present(self.driver, home.submit)
        submit.click()


    def verify_url(self):
        if "https://practicetestautomation.com/logged-in-successfully/" in self.driver.current_url:
            return True
        else:
            return False

    def error(self):
        text = Wait.present(self.driver, home.error)
        return text

class Login:
    def __init__(self, driver):
        self.driver = driver

    def verify_text(self):
        text = Wait.present(self.driver, page.text)
        if text.is_displayed():
            return True
        else:
            return False

    def verify_button(self):
        button = Wait.present(self.driver, page.logout)
        return button