from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_slow_calculator():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()
    driver.implicitly_wait(4)

    delay = driver.find_element(By.CSS_SELECTOR, '#delay')
    delay.clear()
    delay.send_keys('45')

    driver.find_element(By.XPATH, "//span[contains(text(),'C')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'7')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'+')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'8')]").click()
    sleep(4)
    driver.find_element(By.XPATH, "//span[contains(text(),'=')]").click()

    waiter = WebDriverWait(driver, 48) 
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), text_='15'))
    
    result = driver.find_element(By.CSS_SELECTOR,'.screen')
    assert result.text == '15'  

    driver.quit()