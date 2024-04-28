from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def __init__(self, browser):
        self.driver_ = browser

    def get(self):   
        self.driver_.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver_, 10)
        self.driver_.maximize_window()

    def authoriz_form(self): 
        self.driver_.find_element(By.CSS_SELECTOR, '#user-name').send_keys("standard_user")   
        self.driver_.find_element(By.CSS_SELECTOR, '#password').send_keys("secret_sauce")

    def login_button(self):
        self.driver_.find_element(By.CSS_SELECTOR, '#login-button').click()

    def add_products(self): 
        self.driver_.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()  
        self.driver_.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver_.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    def shopping_cart_link(self):          
        self.driver_.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

    def confirmation(self):   
        self.driver_.find_element(By.CSS_SELECTOR, '#checkout').click()
    
    def post_send_key(self):
        self.driver_.find_element(By.CSS_SELECTOR, '#first-name').send_keys("Svetlana")
        self.driver_.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Svetlana")  
        self.driver_.find_element(By.CSS_SELECTOR, '#postal-code').send_keys("142200") 

    def to_click(self):   
        self.driver_.find_element(By.CSS_SELECTOR, '#continue').click()

    def time_waiter(self):
        waiter = WebDriverWait(self.driver_,10) 
        result = waiter.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'summary_total_label'))).text
        return (result)