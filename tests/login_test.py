from selenium import webdriver
import pytest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from utils import utils as utils
import time
import allure
import moment


@pytest.mark.usefixtures("test_setup")
class TestLogin():
    global driver
    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            logout = HomePage(driver)
            logout.click_welcome()
            logout.click_logout_link()
            x = driver.title
            assert x == "OrangeHRM"
        except AssertionError as error:
            driver = self.driver
            print("Assertion error occurred")
            print(error)
            currTime =moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName+" "+currTime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/Nihal/PycharmProjects/AutomationFramework_1/screenshots" + screenshotName + ".png")
            raise
        except:
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + " " + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            print("There was an exception")
            raise
        else:
            print("No exception")
        finally:
            print("Finally Block")
        time.sleep(2)

