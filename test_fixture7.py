import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def dr():
    print("\nstart dr for test..")
    dr = webdriver.Chrome()
    yield dr
    print("\nquit dr..")
    dr.quit()


languages = [
    ("ru", "русский"),
    ("de", "немецкий"),
    pytest.param("ua", "украинский", marks=pytest.mark.xfail(reason="no ua language")),
    ("en-gb", "английский")
]


@pytest.mark.parametrize("code, lang", languages)
def test_guest_should_see_login_link(dr, code, lang):
    link = "http://selenium1py.pythonanywhere.com/{}/".format(code)
    print("Проверяемый язык %s" % lang)
    dr.get(link)
    dr.find_element_by_css_selector("#login_link")