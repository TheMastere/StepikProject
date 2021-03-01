from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открыть нужную страницу
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_id("book").click()

    # Проскроллить страничку и считать значение переменной х
    browser.execute_script("window.scrollBy(0, 300);")
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)

    # Посчитать математическую функцию от x, Ввести ответ в текстовое поле.
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)

    # Отправляем заполненную форму
    browser.find_element_by_css_selector("[type=submit]").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # выходим из браузера
    browser.quit()

