from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_parameters_form():

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.find_element(By.NAME, 'first-name').send_keys("Иван")   
    driver.find_element(By.NAME, 'last-name').send_keys("Петров")
    driver.find_element(By.NAME, 'address').send_keys("Ленина, 55-3")    
    driver.find_element(By.NAME, 'zip-code').send_keys("")
    driver.find_element(By.NAME, 'city').send_keys("Москва")    
    driver.find_element(By.NAME, 'country').send_keys("Россия")
    driver.find_element(By.NAME, 'e-mail').send_keys("test@skypro.com")
    driver.find_element(By.NAME, 'phone').send_keys("+7985899998787")
    driver.find_element(By.NAME, 'job-position').send_keys("QA")
    driver.find_element(By.NAME, 'company').send_keys('SkyPro')
    sleep(4)
    driver.find_element(By.CSS_SELECTOR, 'button').click()
   
    color_zip_code = driver.find_element(
        By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")             
    assert color_zip_code == 'rgba(248, 215, 218, 1)' 

    other_input_fields = ["#first-name", "#last-name", "#address", "#city", "#country",
                         "#e-mail", "#phone", "#job-position", "#company"]
    for field in other_input_fields:
        field_color = driver.find_element(By.CSS_SELECTOR, field).value_of_css_property("background-color")
        assert field_color == 'rgba(209, 231, 221, 1)'

    driver.quit()