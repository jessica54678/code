import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:\Selenium\chromedriver.exe"))
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Alerts.html")


#firstAlert = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a")
#firstAlert.click()

#button1 = driver.find_element(By.XPATH, '//*[@id="OKTab"]/button')
#button1.click()
#time.sleep(3)

#driver.switch_to.alert.accept()

#secondAlert = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a')
#secondAlert.click()
#time.sleep(3)

#button2 = driver.find_element(By.XPATH, '//*[@id="CancelTab"]/button')
#button2.click()
#time.sleep(3)
#driver.switch_to.alert.dismiss()
#time.sleep(5)

promptAlert = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a')
promptAlert.click()
time.sleep(3)

button3 = driver.find_element(By.XPATH, '//*[@id="Textbox"]/button')
button3.click()
time.sleep(3)

driver.switch_to.alert.send_keys("Jess")
driver.switch_to.alert.accept()
time.sleep(5)

