from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    print(x)


    # Посчитать математическую функцию от x, Ввести ответ в текстовое поле.
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    print(y)

    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    browser.find_element_by_css_selector("[for='robotsRule']").click()

    # Отправляем заполненную форму
    browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # выходим из браузера
    browser.quit()