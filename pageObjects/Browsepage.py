from locators.browsepage import Browsepage as browse
# from locators.homepage import Login as page
from selenium.webdriver.common.keys import Keys
from utilities.Wait import Wait

class BrowsePage:
    def __init__(self, driver):
        self.driver = driver

    def search(self, search):
        box = Wait.clickable(self.driver, browse.search_box)
        box.send_keys(search+ Keys.RETURN)

    def confirm(self):
        confirm = Wait.clickable(self.driver, browse.item )
        confirm.click()

    def storage(self, storage):
        if storage == "128 GB":
            storage = Wait.clickable(self.driver, browse.storage_128GB)
        elif storage == "256 GB":
            storage = Wait.clickable(self.driver, browse.storage_256GB)
        else:
            storage = Wait.clickable(self.driver, browse.storage_512GB)
        storage.click()

    def color(self, color):
        if color == "White":
            color = Wait.clickable(self.driver, browse.color_white)
        color.click()

    def buy_now(self):
        buy = Wait.clickable(self.driver, browse.buy)
        buy.click()
    def place_order(self):
        place_order = Wait.clickable(self.driver, browse.order)
        place_order.click()

    def add_to_cart(self):
        add_to_cart = Wait.clickable(self.driver, browse.cart)
        add_to_cart.click()

    def buy(self, search):
        buy = Wait.clickable(self.driver, browse.buy)
        buy.click()

    # def get_password(self, password):
    #     box = Wait.clickable(self.driver, browse.password)
    #     box.send_keys(password)

    def click_submit(self):
        submit = Wait.present(self.driver, browse.submit)
        submit.click()

