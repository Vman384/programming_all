from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Using Chrome to access web
driver = webdriver.Chrome()
# Open the website
driver.get('https://www.cellopark.com.au/CustomerOffice/Account/LoginView')

driver.implicitly_wait(5)
# Equivalent Outcome! 
id_box = driver.find_element('name','UserName')

# Send id information
id_box.send_keys('0424284945')

driver.implicitly_wait(10)

# Find password box
pass_box = driver.find_element('name',value='Password')
# Send password
pass_box.send_keys('MyCellopark1')
# Find login button
login_button = driver.find_element(by=By.XPATH, value='//*[@id="login-form"]/div[2]/div[2]/footer/button')
# Click login
login_button.click()
driver.implicitly_wait(10)


live_parking = driver.find_element(by=By.ID, value='liveParkingBtn')
live_parking.click()
driver.implicitly_wait(10)

location = driver.find_element(by=By.XPATH, value='//*[@id="City"]/paper-input-container/div[2]/iron-icon[2]')
driver.implicitly_wait(20)

location.click()
uni = driver.find_element(by=By.XPATH,value='//*[@id="CitiesMenu"]/li[16]/a')
uni.click()
zone = driver.find_element(by=By.XPATH, value='//*[@id="Zone"]/paper-input-container/div[2]/iron-icon[2]')
zone.click()
zone = driver.find_element(by=By.XPATH, value='//*[@id="SubZonesMenu"]/li[8]/a')
zone.click()

start = driver.find_element(by=By.ID, value='StartStopBtn')
start.click()
input()
