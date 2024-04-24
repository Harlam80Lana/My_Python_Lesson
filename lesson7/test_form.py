
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from class_form_page import FormPage

def test_form():

    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    form_page = FormPage(browser)   
    form_page.get()
    form_page.input_text()
    form_page.submit()

    red = form_page.result_red()
    assert red == 'rgba(248, 215, 218, 1)'

    green = form_page.result_green()
    assert green == 'rgba(209, 231, 221, 1)'

    browser.quit()                              