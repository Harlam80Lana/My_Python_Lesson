from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Модальное окно
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/entry_ad")
driver.find_element(By.CSS_SELECTOR,"[class='modal']")
sleep(1)
driver.find_element(By.CSS_SELECTOR,"[class='modal-footer']").click()
driver.close()