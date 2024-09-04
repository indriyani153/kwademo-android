from appium.webdriver.common.appiumby import AppiumBy
from locators.home_locator import HomeLocator

class Homepage:

    def __init__(self,driver):
        self.driver = driver
    
    def click_login(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, HomeLocator.login_button).click()

    def click_enter_some_value(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, HomeLocator.enter_value_button).click()
    
    def click_contact(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, HomeLocator.contactus_button).click()
    
