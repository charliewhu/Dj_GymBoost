from selenium.webdriver.common.by import By


def get_inner_html(context, id):
    element = context.browser.find_element(By.ID, id)
    return element.get_attribute("innerHTML")
