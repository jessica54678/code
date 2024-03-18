
import unittest
import time
from Page.loginPage import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=Service("C:/Selenium/chromedriver.exe"))
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com/")

    def testa(self):
        lp = LoginPage(self.driver)
        lp.pageLogin()
        time.sleep(10)
        expected = "Welcome testmorning"
        actual = self.driver.find_element(By.ID, 'nameofuser').text
        self.assertEqual(expected, actual, "This doesnot match")

    def test_b(self):
        lp = LoginPage(self.driver)
        lp.pageLogin()

    def test_a(self):
        print("This is test2")

    @classmethod
    def tearDownClass(self):
        print("This is run after")
