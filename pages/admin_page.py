from appium.webdriver.common.appiumby import AppiumBy
from locators.admin_locator import AdminLocator

class AdminPage:

    def __init__(self, driver):
        self.driver = driver
    
    def check_text(self):
        text = self.driver.find_element(AppiumBy.XPATH, AdminLocator.text_enter_admin).text

        return text