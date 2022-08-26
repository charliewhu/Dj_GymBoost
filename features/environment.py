from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Firefox()
    context.browser.get("http://127.0.0.1:8000/")


def after_all(context):
    context.browser.quit()


def before_feature(context, feature):
    context.browser.get("http://127.0.0.1:8000/")
