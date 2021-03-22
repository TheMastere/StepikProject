from selenium import webdriver
import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:
    @pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                       "https://stepik.org/lesson/236896/step/1",
                                       "https://stepik.org/lesson/236897/step/1",
                                       "https://stepik.org/lesson/236898/step/1",
                                       "https://stepik.org/lesson/236899/step/1",
                                       "https://stepik.org/lesson/236903/step/1",
                                       "https://stepik.org/lesson/236904/step/1",
                                       "https://stepik.org/lesson/236905/step/1"])
    def test_for_correct_answer(self, browser, links):
        browser.get(links)
        answer = str(math.log(+int(time.time())))
        button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".textarea")))
        button.send_keys(answer)
        # Отправляем заполненную форму
        browser.find_element_by_css_selector(".submit-submission").click()
        browser.implicitly_wait(5)
        answer_text = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert answer_text == 'Correct!'
