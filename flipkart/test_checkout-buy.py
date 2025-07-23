import time

import pytest

from pageObjects.Browsepage import *
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Test_add_to_cart(BaseClass):

    # @pytest.mark.negative
    # @pytest.mark.negative_v1
    # def test_negative_v1(self):
    #     log = self.get_logger()
    #     log.info("--test negative 1--")
    #     browse = HomePage(self.driver)
    #     homepage.get_user("incorrectUser")
    #     homepage.get_password("Password123")
    #     homepage.click_submit()
    #     if homepage.error().is_displayed():
    #         log.info("msg displayed")
    #     else:
    #         log.info("msg not displayed")
    #     if homepage.error().text == "Your username is invalid!":
    #         log.info("correct error msg")
    #     else:
    #         log.info("incorrect msg")
    #     log.info("--test end--")
    #
    #
    #
    # @pytest.mark.negative
    # @pytest.mark.negative_v2
    # def test_negative_v2(self):
    #     log = self.get_logger()
    #     log.info("--test negative 2--")
    #     homepage = HomePage(self.driver)
    #     homepage.get_user("student")
    #     homepage.get_password("incorrectPassword")
    #     homepage.click_submit()
    #     if homepage.error().is_displayed():
    #         log.info("msg displayed")
    #     else:
    #         log.info("msg not displayed")
    #
    #     if homepage.error().text == "Your password is invalid!":
    #         log.info("correct msg")
    #     else:
    #         log.info("incorrect msg")


    @pytest.mark.positive
    def test_positive_addtocart(self):
        log = self.get_logger()
        log.info("--test positive--")
        browse = BrowsePage(self.driver)
        browse.search("iphone 16")
        browse.confirm()
        self.driver.switch_to.window(self.driver.window_handles[1])
        log.info("found iphone 16")

        browse.storage("512 GB")
        # browse.color("White")
        log.info("found desired variant")

        # if browse.buy_now():
        #     log.info("--test buy now--")
        browse.add_to_cart()
        log.info("Variant is_available")
        log.info("item added to cart")
        time.sleep(2)
        browse.place_order()

        log.info("--test end--")

