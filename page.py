from element import BasePageElement
from locators import MainPageLocators,SecondPageLocators
from selenium.webdriver.support.ui import Select



class Element(BasePageElement):
    """This class gets the element from the specified locator"""
    locator = ("","")
    def __init__(self,type:str,name:str):
        self.locator = (type,name)
    


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    fname = Element("id","fname")
    lname = Element("id","lname")
    dob = Element("id","dob")
    email = Element("id","email")
    country = Element("id","country")
    mobile = Element("id","mobile")
    aby = Element("css selector","#automationtestform > div:nth-child(1) > div:nth-child(11) > textarea")
    uname = Element("css selector","#automationtestform > div:nth-child(2) > div.col-xs-12 > div > div.col-xs-6 > div > div > input")
    pwd = Element("css selector","#automationtestform > div:nth-child(2) > div:nth-child(2) > div > div > input")
    cpwd = Element("css selector","#automationtestform > div:nth-child(2) > div:nth-child(3) > div > div > input")




    def is_form_present(self):
        """Verifies if form is present"""
        return self.driver.find_elements(*MainPageLocators.FORM_TAG)

    def click_submit_button(self):
        element = self.driver.find_element(*MainPageLocators.SUBMIT_BUTTON)
        element.click()
    
    def click_agree_button(self):
        element = self.driver.find_element(*MainPageLocators.AGREE)
        element.click()
    
    def click_hobbies_button(self):
        element = self.driver.find_element(*MainPageLocators.HOBBIES)
        element.click()
    
    def select_state_button(self,nation:str):
        select = Select(self.driver.find_element(*MainPageLocators.SELECT))
        select.select_by_value(nation)

    def is_submission_succesful(self):
        return self.driver.current_url == "https://app.cloudqa.io/Home/AutomationPracticeForm"

    def click_male_button(self):
        element = self.driver.find_element(*MainPageLocators.GENDER)
        element.click()

    
class SecondPage(BasePage):
    def is_pre_present(self):
        return self.driver.find_elements(*SecondPageLocators.PRE)
    def get_pre_in_dict(self):
        x =  self.driver.find_element(*SecondPageLocators.PRE)
        return x.text

        


