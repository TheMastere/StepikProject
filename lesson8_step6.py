from selenium import webdriver
import time
import math

    # Открыть страницу http://suninjuly.github.io/get_attribute.html
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение переменной х
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)

    # Посчитать математическую функцию от x, Ввести ответ в текстовое поле.
    def calc(x):
        return str(math.log(abs(12*math.sin(x))))

    y = calc(x)

    # Ввести ответ в текстовое поле. Прокрутить страничку внизу.
    # Отметить checkbox "Подтверждаю, что являюсь роботом". Выбрать radiobutton "Роботы рулят!".
    browser.find_element_by_id('answer').send_keys(y)
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()

    # Отправляем заполненную форму
    browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # выходим из браузера
    browser.quit()

