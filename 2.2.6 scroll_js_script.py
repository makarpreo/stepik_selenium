#https://SunInJuly.github.io/execute_script.html
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from math import *
link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element(By.ID, 'input_value').text)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(log(abs(12*sin(x)), e))
    submit_button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    button = browser.find_element(By.ID, 'robotCheckbox')
    button.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
