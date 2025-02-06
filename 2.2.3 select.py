
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)
    print(num2, num1, num1+num2)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(f"{num1 + num2}")
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
