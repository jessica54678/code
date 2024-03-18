import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginTestCase(unittest.TestCase):

    def setUp(self):
        print("This is first")
        self.driver = webdriver.Chrome(service=Service("C:/Selenium/chromedriver.exe"))
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com/")

    def test_login(self):
        print("This is test")
        driver = self.driver
        LogIn = self.driver.find_element(By.ID, "login2")
        LogIn.click()
        usernameform = driver.find_element(By.ID, "loginusername")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(usernameform))
        usernameform.send_keys("testmorning")
        passwordform = driver.find_element(By.ID, "loginpassword")
        passwordform.send_keys("test123")
        loginButton = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        loginButton.click()
        time.sleep(10)

        expected = "Welcome testmorning"
        actual = driver.find_element(By.ID, 'nameofuser').text
        self.assertEqual(expected, actual, "This doesnot match")

    def tearDown(self):
        print("This is after")
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
