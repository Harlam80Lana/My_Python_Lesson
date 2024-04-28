from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from form_page import FormPage
                                                        # pytest -v form_green_test.py
def test_green_form():

    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    form_page = FormPage(browser)   
    form_page.get()
    form_page.input_text()
    form_page.submit()

    other_input_fields = ["#first-name", "#last-name", "#address", "#city", "#country",
                            "#e-mail", "#phone", "#job-position", "#company"]
    for field in other_input_fields:
        green = form_page.result_green(field)

        assert green == 'rgba(209, 231, 221, 1)'

    browser.quit()                              