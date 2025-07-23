import time

import pytest

from pageObjects.Homepage import *
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Test_Login(BaseClass):

    @pytest.mark.negative
    @pytest.mark.negative_v1
    def test_negative_v1(self):
        log = self.get_logger()
        log.info("--test negative 1--")
        homepage = HomePage(self.driver)
        homepage.get_user("incorrectUser")
        homepage.get_password("Password123")
        homepage.click_submit()
        if homepage.error().is_displayed():
            log.info("msg displayed")
        else:
            log.info("msg not displayed")
        if homepage.error().text == "Your username is invalid!":
            log.info("correct error msg")
        else:
            log.info("incorrect msg")
        log.info("--test end--")



    @pytest.mark.negative
    @pytest.mark.negative_v2
    def test_negative_v2(self):
        log = self.get_logger()
        log.info("--test negative 2--")
        homepage = HomePage(self.driver)
        homepage.get_user("student")
        homepage.get_password("incorrectPassword")
        homepage.click_submit()
        if homepage.error().is_displayed():
            log.info("msg displayed")
        else:
            log.info("msg not displayed")

        if homepage.error().text == "Your password is invalid!":
            log.info("correct msg")
        else:
            log.info("incorrect msg")


    @pytest.mark.positive
    def test_positive(self):
        log = self.get_logger()
        log.info("--test positive--")
        homepage = HomePage(self.driver)
        homepage.get_user("student")
        homepage.get_password("Password123")
        homepage.click_submit()
        log.info("clicked on submit")
        if homepage.verify_url():
            log.info("verified url")
        else:
            log.info("url unverified")
        login = Login(self.driver)
        if login.verify_text():
            log.info("text present")
        else:
            log.info("text absent")
        if login.verify_button().is_displayed():
            log.info("log out button present")
        else:
            log.info("button not present")

        log.info("--test end--")

