import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,"price"), "100"))

button = browser.find_element(By.ID, 'book').click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

text = browser.find_element(By.ID, 'answer')
text.send_keys(y)

html = browser.find_element(By.TAG_NAME, "html")
html.send_keys(Keys.END)

button2 = browser.find_element(By.ID, 'solve').click()

browser.quit()