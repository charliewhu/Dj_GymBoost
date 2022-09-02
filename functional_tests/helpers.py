from selenium.webdriver.common.by import By


def get_inner_html(context, id):
    element = context.browser.find_element(By.ID, id)
    return element.get_attribute("innerHTML")


def get_by_text(context, text: str):
    return context.browser.find_element(By.XPATH, f"//*[contains(text(), '{text}')]")
