from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from calculator_page import CalculatorPage
                                                   # pytest calculator_test.py
def test_slow_calculator():                      
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    calculator_page = CalculatorPage(browser)          
    calculator_page.delay(45)
    calculator_page.input_text(7, 8)
    calculator_page.time_waiter()

    # Универсальный вариант:
    #calculator_page.input_text('C7+8=')

    result = calculator_page.result_text
    assert result() == '15'

    browser.quit()   