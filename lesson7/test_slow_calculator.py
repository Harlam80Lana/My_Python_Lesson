from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from class_calculator_page import CalculatorPage

def test_slow_calculator():                      
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    calculator_page = CalculatorPage(browser)          
    calculator_page.delay()
    calculator_page.input_text()
    calculator_page.time_waiter()

    result = calculator_page.result_text

    assert result() == '15'

    browser.quit()   
