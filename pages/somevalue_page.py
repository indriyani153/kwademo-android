from appium.webdriver.common.appiumby import AppiumBy
from locators.somevalue_locator import ValueLocator
from data.data_value import EnterValue

class ValuePage:
    def __init__(self,driver):
        self.driver = driver

    def input_value(self):
        self.driver.find_element(AppiumBy.ID, ValueLocator.enter_value).send_keys(EnterValue.value)
    
    def click_submit(self):
        self.driver.find_element(AppiumBy.ID, ValueLocator.btn_submit).click()

    def prev(self):
        text = self.driver.find_element(AppiumBy.ID, ValueLocator.preview).text

        return text