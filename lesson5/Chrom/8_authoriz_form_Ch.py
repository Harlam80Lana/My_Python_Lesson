#from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Форма авторизации
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")
# search_field = '#username'
# search_input = driver.find_element(By.CSS_SELECTOR, search_field)
# search_input.send_keys("tomsmith")
# search_field = '#password'
# search_input = driver.find_element(By.CSS_SELECTOR, search_field)
# search_input.send_keys("SuperSecretPassword!")
# driver.find_element(By.CSS_SELECTOR,"[class='radius']").click()
# driver.close()
field_username = driver.find_element(By.CSS_SELECTOR, '#username')
field_username.send_keys("tomsmith")
field_password = driver.find_element(By.CSS_SELECTOR, '#password')
field_password.send_keys("SuperSecretPassword!")
login_button = driver.find_element(By.CSS_SELECTOR,"[class='radius']")
login_button.click()
driver.close()