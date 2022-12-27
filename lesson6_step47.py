from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("таня")
    input1 = browser.find_element(By.NAME, "lastname")
    input1.send_keys("никонова")
    input1 = browser.find_element(By.NAME, "email")
    input1.send_keys("www.tanya98@mail.ru")
    element  = browser.find_element(By.ID, "file") 
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()




