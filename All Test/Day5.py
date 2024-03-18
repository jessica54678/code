import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException

try:
    driver = webdriver.Chrome(service=Service("C:\Selenium\chromedriver.exe"))
    driver.maximize_window()
    driver.get("https://demoblaze.com/")

    LogIn = driver.find_element(By.ID, "login2")
    LogIn.click()
    usernameform = driver.find_element(By.ID, "loginusern")
    # WebDriverWait(driver,10).until(EC.element_to_be_clickable(usernameform))
    usernameform.send_keys("testmorning")
    passwordform = driver.find_element(By.ID, "loginpassword")
    passwordform.send_keys("test123")
    loginButton = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    loginButton.click()
    time.sleep(10)

except ElementNotInteractableException as e:
    print("The try did not work")

    try:
        driver.implicitly_wait(10)
        usernameform = driver.find_element(By.ID, "loginusername")
    # WebDriverWait(driver,10).until(EC.element_to_be_clickable(usernameform))
        usernameform.send_keys("testmorning")
        passwordform = driver.find_element(By.ID, "loginpassword")
        passwordform.send_keys("test123")
        loginButton = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        loginButton.click()
        time.sleep(10)


    except ElementNotInteractableException as e:
        print("I am running from exception")
        driver.implicitly_wait(10)
        usernameform = driver.find_element(By.ID, "loginusername")
        # WebDriverWait(driver,10).until(EC.element_to_be_clickable(usernameform))
        usernameform.send_keys("testmorning")
        passwordform = driver.find_element(By.ID, "loginpassword")
        passwordform.send_keys("test123")
        loginButton = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        loginButton.click()
        time.sleep(10)

except NoSuchElementException as E:
    print("I am running from exception")
    driver.implicitly_wait(10)
    usernameform = driver.find_element(By.ID, "loginusername")
    # WebDriverWait(driver,10).until(EC.element_to_be_clickable(usernameform))
    usernameform.send_keys("testmorning")
    passwordform = driver.find_element(By.ID, "loginpassword")
    passwordform.send_keys("test123")
    loginButton = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    loginButton.click()
    time.sleep(10)


