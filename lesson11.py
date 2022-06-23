from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

text = browser.find_element(By.XPATH, '//*[@id="answer"]')
text.send_keys(y)

not_robot = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]').click()
robots_rule = browser.find_element(By.CSS_SELECTOR, "[value=robots]")
robots_rule.click()
button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
button.click()

time.sleep(5)
browser.quit()



