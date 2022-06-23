from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

text = browser.find_element(By.ID, 'answer')
text.send_keys(y)
checkbox = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]').click()
radiobutton = browser.find_element(By.CSS_SELECTOR, "[value=robots]").click()
button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
time.sleep(5)
browser.quit()