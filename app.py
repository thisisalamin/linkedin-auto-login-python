from selenium import webdriver
from selenium.webdriver.common.keys import Keys

emailOrPhone = "yourusername"
password = "yourpass"

driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://www.linkedin.com/login')

username_field = driver.find_element_by_id('username')
username_field.send_keys(emailOrPhone)

password_field = driver.find_element_by_id('password')
password_field.send_keys(password)

signin = driver.find_element_by_tag_name('button')
signin.click()
