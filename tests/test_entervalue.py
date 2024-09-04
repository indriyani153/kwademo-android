
from settings.initiation import *
from appium.webdriver.common.appiumby import AppiumBy

from data.data_value import *
from pages.home_page import *
from pages.somevalue_page import *


@pytest.fixture
def setup():
    driver = Inisiasi.init_driver()
    yield driver
    driver.quit()

def test_enter_value_1(setup):
    homepage = Homepage(setup)
    valuepage = ValuePage(setup)

    homepage.click_enter_some_value()
    valuepage.input_value()
    valuepage.click_submit()

    text = valuepage.prev()

    assert text == EnterValue.value