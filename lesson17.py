import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()

handles = browser.window_handles
browser.switch_to.window(handles[1])

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

text = browser.find_element(By.ID, 'answer')
text.send_keys(y)

button = browser.find_element_by_css_selector("button.btn").click()

time.sleep(8)
browser.quit()