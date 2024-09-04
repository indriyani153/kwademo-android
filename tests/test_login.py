
from settings.initiation import *
from appium.webdriver.common.appiumby import AppiumBy

from pages.home_page import *
from pages.login_page import *
from pages.admin_page import *


@pytest.fixture
def setup():
    driver = Inisiasi.init_driver()
    yield driver
    driver.quit()

def test_login_positive(setup):
    homepage = Homepage(setup)
    loginpage = LoginPage(setup)
    adminpage = AdminPage(setup)

    homepage.click_login()
    loginpage.input_username()
    loginpage.input_password()
    loginpage.click_submit()

    text = adminpage.check_text()

    assert text == 'Enter Admin'