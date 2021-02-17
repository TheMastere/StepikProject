from selenium import webdriver
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector("[name=firstname]")
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_css_selector("[name=lastname]")
    last_name.send_keys("Petrov")
    email = browser.find_element_by_css_selector("[name=email]")
    email.send_keys("Smolensk123@mail.ru")

    # Передаем путь к файлу и загружаем файл в форму для загрузки файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'masterfile.txt')
    upload_file = browser.find_element_by_css_selector("[type=file]").send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()