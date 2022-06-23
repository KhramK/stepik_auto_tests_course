import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

first_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
first_name.send_keys('Max')

last_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
last_name.send_keys('Petrov')

email = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
email.send_keys('123@gmal.com')

chooseFile = browser.find_element(By.XPATH, '//*[@id="file"]')
chooseFile.send_keys('C:/1/123.txt')

button = browser.find_element_by_css_selector("button.btn").click()

#time.sleep(3)
#browser.quit()