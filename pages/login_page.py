from appium.webdriver.common.appiumby import AppiumBy
from locators.login_locator import LoginLocator
from data.data_io import LoginData

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
    
    def input_username(self):
        self.driver.find_element(AppiumBy.ID, LoginLocator.username).send_keys(LoginData.username)
    
    def input_password(self):
        self.driver.find_element(AppiumBy.ID, LoginLocator.password).send_keys(LoginData.password)

    def click_submit(self):
        self.driver.find_element(AppiumBy.ID, LoginLocator.submit).click()