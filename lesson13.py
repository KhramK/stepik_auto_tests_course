from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element(By.ID, 'num1').text
y = browser.find_element(By.ID, 'num2').text

z = (int(x)+int(y))

dropdown = browser.find_element(By.ID, 'dropdown').click()
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(z))
button = browser.find_element_by_css_selector("button.btn").click()



time.sleep(5)
browser.quit()