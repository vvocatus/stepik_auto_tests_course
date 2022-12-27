from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def sum(x, y):
  return str(x + y)

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = y_element.text 
    z = str(int(x) + int(y))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


