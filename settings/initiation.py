import pytest
from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options

class Inisiasi:
    def init_driver():
        options = UiAutomator2Options()

        options.udid = 'RR8M50ASSET'
        options.platform_name = 'Android'
        options.app_package = 'com.code2lead.kwad'
        options.app_activity = 'com.code2lead.kwad.MainActivity'

        driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
        driver.implicitly_wait(50)

        return driver 