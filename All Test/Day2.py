import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:\Selenium\chromedriver.exe"))
driver.maximize_window()
driver.get("https://demoblaze.com/")

LogIn = driver.find_element(By.ID, "login2")
LogIn.click()
usernameform = driver.find_element(By.ID, "loginusername")
time.sleep(5)
usernameform.send_keys("testmorning")
passwordform = driver.find_element(By.ID, "loginpassword")
passwordform.send_keys("test123")
loginButton = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
loginButton.click()
time.sleep(10)


