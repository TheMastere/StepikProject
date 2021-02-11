from selenium import webdriver
import time
import math

    # Открыть страницу http://suninjuly.github.io/get_attribute.html
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти на ней элемент-картинку/ Взять у этого элемента значение атрибута valuex
    x_element = browser.find_element_by_id("treasure").get_attribute("valuex")
    x = int(x_element)
    print(x)

    # Посчитать математическую функцию от x, Ввести ответ в текстовое поле.
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)

    # Ввести ответ в текстовое поле. Отметить checkbox "Подтверждаю, что являюсь роботом". Выбрать radiobutton "Роботы рулят!".
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()

    # Отправляем заполненную форму
    browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # выходим из браузера
    browser.quit()
