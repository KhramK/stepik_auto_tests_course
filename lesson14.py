from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

ok = browser.find_element(By.XPATH, '//*[@id="answer"]')
ok.send_keys(y)

checkbox = browser.find_element(By.CLASS_NAME, 'form-check-input').click()
radiobutton = browser.find_element(By.ID, 'robotsRule').click()

button = browser.find_element_by_css_selector("button.btn").click()