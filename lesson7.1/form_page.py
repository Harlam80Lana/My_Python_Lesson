from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class FormPage:

    def __init__(self, browser):
        self.driver_ = browser

    def get(self):   
        self.driver_.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        WebDriverWait(self.driver_, 10)
                                                                                
    def input_text(self):
        self.driver_.find_element(By.NAME, 'first-name').send_keys("Иван")                               
        self.driver_.find_element(By.NAME, 'last-name').send_keys("Петров")
        self.driver_.find_element(By.NAME, 'address').send_keys("Ленина, 55-3")    
        self.driver_.find_element(By.NAME, 'zip-code').send_keys("")
        self.driver_.find_element(By.NAME, 'city').send_keys("Москва")    
        self.driver_.find_element(By.NAME, 'country').send_keys("Россия")
        self.driver_.find_element(By.NAME, 'e-mail').send_keys("test@skypro.com")
        self.driver_.find_element(By.NAME, 'phone').send_keys("+7985899998787")
        self.driver_.find_element(By.NAME, 'job-position').send_keys("QA")
        self.driver_.find_element(By.NAME, 'company').send_keys('SkyPro')

    def submit(self):
        self.driver_.find_element(By.CSS_SELECTOR, 'button').click()
    
    def result_green(self, fil):
        field_color = self.driver_.find_element(
            By.CSS_SELECTOR, fil).value_of_css_property("background-color")
        return(field_color)
    
    def result_red(self):
        color_zip_code = self.driver_.find_element(
            By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
        return(color_zip_code) 