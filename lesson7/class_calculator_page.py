from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, browser):
        self.driver_ = browser
        self.driver_.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        WebDriverWait(self.driver_,4)
        self.driver_.maximize_window()

    def delay(self):    
        delay = self.driver_.find_element(By.CSS_SELECTOR, '#delay')
        delay.clear()
        delay.send_keys('45')

    def input_text(self):
        self.driver_.find_element(By.XPATH, "//span[contains(text(),'C')]").click()
        self.driver_.find_element(By.XPATH, "//span[contains(text(),'7')]").click()
        self.driver_.find_element(By.XPATH, "//span[contains(text(),'+')]").click()
        self.driver_.find_element(By.XPATH, "//span[contains(text(),'8')]").click()
        self.driver_.find_element(By.XPATH, "//span[contains(text(),'=')]").click()

    def time_waiter(self):
        waiter = WebDriverWait(self.driver_,48) 
        waiter.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), text_='15'))

    def result_text(self):
        result = self.driver_.find_element(By.CSS_SELECTOR,'.screen')
        return result.text