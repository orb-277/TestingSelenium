import unittest
from selenium import webdriver
import page
import json

import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    match = re.match(pattern, email)
    return match is not None



class Form(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")

    def tearDown(self):
        self.driver.close()
    
    def test_form_fill(self):
        main_page = page.MainPage(self.driver)
        second_page = page.SecondPage(self.driver)
        # self.assertTrue(main_page.is_title_matches(), "title doesn't match.")
        self.assertTrue(main_page.is_form_present(),"form not present")
        main_page.fname = "My Name"
        main_page.lname = "Last"
        main_page.dob = "1992-12-12"
        main_page.email = "asdas@gmail.com"
        main_page.country = "adsfas"
        main_page.uname ="asdasuser"
        main_page.pwd = "1234"
        main_page.cpwd = "1234"
        main_page.aby = "Hi its mee"
        main_page.mobile = "1234567890"
        main_page.click_agree_button()
        main_page.click_hobbies_button()
        main_page.click_male_button()
        
        main_page.select_state_button("Cuba")
        main_page.click_submit_button()

        self.assertTrue(main_page.is_submission_succesful(),"form submission failure")
        self.assertTrue(second_page.is_pre_present(),"pre not present")
        # self.assertTrue(main_page.pwd.text == main_page.cpwd.text,"passwords do not match")
        data = json.loads(second_page.get_pre_in_dict())
        self.assertTrue(data["Password"]==data["Confirm Password"],"Password didn't match")
        self.assertTrue(len(data["Mobile Number"])==10,"mobile not valid")
        self.assertTrue(is_valid_email(data["Email"]),"not valid email")
        self.assertTrue(data!="-- Select Country --","Country not selected")

    def test_form_fill2(self):
        main_page = page.MainPage(self.driver)
        second_page = page.SecondPage(self.driver)
        # self.assertTrue(main_page.is_title_matches(), "title doesn't match.")
        self.assertTrue(main_page.is_form_present(),"form not present")
        main_page.fname = "My Name"
        main_page.lname = "Last"
        main_page.dob = "2002-12-12"
        main_page.email = "asdas@gmail.com"
        main_page.country = "India"
        main_page.uname ="asdasuser"
        main_page.pwd = "1234"
        main_page.cpwd = "1234"
        main_page.aby = "Hi its mee"
        main_page.mobile = "1234567890"
        main_page.click_agree_button()
        main_page.click_hobbies_button()
        main_page.click_male_button()
        
        main_page.select_state_button("Cuba")
        main_page.click_submit_button()

        self.assertTrue(main_page.is_submission_succesful(),"form submission failure")
        self.assertTrue(second_page.is_pre_present(),"pre not present")
        # self.assertTrue(main_page.pwd.text == main_page.cpwd.text,"passwords do not match")
        data = json.loads(second_page.get_pre_in_dict())
        self.assertTrue(data["Password"]==data["Confirm Password"],"Password didn't match")
        self.assertTrue(len(data["Mobile Number"])==10,"mobile not valid")
        self.assertTrue(is_valid_email(data["Email"]),"not valid email")
        self.assertTrue(data!="-- Select Country --","Country not selected")



if __name__ == "__main__":
    unittest.main()
