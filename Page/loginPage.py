
from selenium.webdriver.common.by import By
from locators.locator import Locate
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.lc = Locate()

    def pageLogin(self):
            driver = self.driver
            LogIn = self.driver.find_element(By.ID, self.lc.LogInID)
            LogIn.click()
            driver.implicitly_wait(10)
            usernameform = self.driver.find_element(By.ID, self.lc.UserNameID)
            usernameform.send_keys("testmorning")

            passwordform = driver.find_element(By.ID, self.lc.passwordID)
            passwordform.send_keys("test123")
            loginButton = driver.find_element(By.XPATH, self.lc.loginXp)
            loginButton.click()
