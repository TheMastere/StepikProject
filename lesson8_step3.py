from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

# Открыть страницу http://suninjuly.github.io/selects1.html
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

# Ищем элементы на открытой странице, складывание чисел и переход их в строку
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    number = str(int(num1) + int(num2))

# Выбор ответа из выпадающего списка и вставка его в поле для ввода
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(number)

# Отправляем заполненную форму
    browser.find_element_by_css_selector("button.btn").click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
finally:
    time.sleep(10)
# выходим из браузер
    browser.quit()