import unittest
import HtmlTestRunner
from selenium import webdriver
import time
import sys
sys.path.append("C:/Users/hp/PycharmProjects/pythonProject4/pythonUnitTestProject_POMBased")
from PagesObjects.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    baseURL="https://opensource-demo.orangehrmlive.com"
    username="Admin"
    password="admin123"
    driver=webdriver.Chrome(executable_path="C:/Users/hp/PycharmProjects/pythonProject4/pythonUnitTestProject_POMBased/Drivers/chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.ClickLogin()
        lp.ClickButton()
        time.sleep(5)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Reports'))



