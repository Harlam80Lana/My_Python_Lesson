from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CalculatorPage:

    def __init__(self, browser):
        self.driver_ = browser
        self.driver_.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        WebDriverWait(self.driver_,4)

    def delay(self, time):    
        delay = self.driver_.find_element(By.CSS_SELECTOR, '#delay')
        delay.clear()
        delay.send_keys(time)

    def input_text(self, num1, num2):
        self.driver_.find_element(By.XPATH, "//span[contains(text(),'C')]").click()
        self.driver_.find_element(By.XPATH, f"//span[contains(text(),'{num1}')]").click()
        self.driver_.find_element(By.XPATH, "//span[contains(text(),'+')]").click()
        self.driver_.find_element(By.XPATH, f"//span[contains(text(),'{num2}')]").click()
        self.driver_.find_element(By.XPATH, "//span[contains(text(),'=')]").click()

    # Универсальный вариант:
    # def input_text(self, keys_calculator):
    #      for val in keys_calculator:
    #         self.driver_.find_element(By.XPATH, f'//span[text()="{val}"]').click()

    def time_waiter(self):
        waiter = WebDriverWait(self.driver_, 48) 
        waiter.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), text_='15'))

    def result_text(self):
        result = self.driver_.find_element(By.CSS_SELECTOR,'.screen')
        return result.text