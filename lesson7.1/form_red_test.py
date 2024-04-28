
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from form_page import FormPage
                                                             # pytest form_red_test.py
def test_form():

    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    form_page = FormPage(browser)   
    form_page.get()
    form_page.input_text()
    form_page.submit()

    red = form_page.result_red()
    assert red == 'rgba(248, 215, 218, 1)'

    browser.quit()                              