from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def before_all(context):
    context.browser = webdriver.Remote(
        "http://selenium:4444/wd/hub", DesiredCapabilities.FIREFOX
    )


def after_all(context):
    context.browser.quit()


def before_feature(context, feature):
    pass
