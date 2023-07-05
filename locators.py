from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-primary[value="submit"]')
    FORM_TAG = (By.ID,'automationtestform')
    SELECT = (By.CSS_SELECTOR,'#state')
    HOBBIES = (By.CSS_SELECTOR,'div.form-group:nth-child(10) > input:nth-child(2)')
    AGREE = (By.CSS_SELECTOR,'#Agree')
    GENDER = (By.ID,'male')



class SecondPageLocators(object):
    PRE = (By.CSS_SELECTOR,'body > div.container > div > div > pre')
