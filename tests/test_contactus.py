from settings.initiation import *
from appium.webdriver.common.appiumby import AppiumBy

from data.data_contact import *
from pages.home_page import *
from pages.contactus_page import *

@pytest.fixture
def setup():
    driver = Inisiasi.init_driver()
    yield driver
    driver.quit()

def test_contactus(setup):
    homepage = Homepage(setup)
    contactus = ContactusPage(setup)

    homepage.click_contact()
    contactus.input_name()
    contactus.input_email()
    contactus.input_address()
    contactus.input_mobileno()
    contactus.click_submit()

    text1 = contactus.out_name()
    text2 = contactus.out_email()
    text3 = contactus.out_address()
    text = contactus.out_mobile()

    assert text1 == (f"Name: {ContactData.name}")
    assert text2 == (f"Email: {ContactData.email}")
    assert text3 == (f"Password: {ContactData.address}")
    assert text == (f"Mobile: {ContactData.mobile}")