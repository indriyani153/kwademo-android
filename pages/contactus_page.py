from appium.webdriver.common.appiumby import AppiumBy
from locators.contactus_locator import ContactLocator
from data.data_contact import ContactData


class ContactusPage:
    def __init__(self,driver):
        self.driver = driver
    
    def input_name(self):
        self.driver.find_element(AppiumBy.ID, ContactLocator.input_name).send_keys(ContactData.name)
    
    def input_email(self):
        self.driver.find_element(AppiumBy.ID, ContactLocator.input_email).send_keys(ContactData.email)
    
    def input_address(self):
        self.driver.find_element(AppiumBy.ID, ContactLocator.input_address).send_keys(ContactData.address)
    
    def input_mobileno(self):
        self.driver.find_element(AppiumBy.ID, ContactLocator.input_mobileno).send_keys(ContactData.mobile)

    def click_submit(self):
        self.driver.find_element(AppiumBy.ID, ContactLocator.click_submit).click()
    
    def out_name(self):
        text = self.driver.find_element(AppiumBy.ID, ContactLocator.check_name).text

        return text
    
    def out_email(self):
        text = self.driver.find_element(AppiumBy.ID, ContactLocator.check_email).text

        return text

    def out_address(self):
        text = self.driver.find_element(AppiumBy.ID, ContactLocator.check_address).text

        return text
    
    def out_mobile(self):
        text = self.driver.find_element(AppiumBy.ID, ContactLocator.check_mobile).text

        return text
    
