from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


# Модальное окно
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/entry_ad")
driver.find_element(By.CSS_SELECTOR,"[class='modal']")
sleep(1)
driver.find_element(By.CSS_SELECTOR,"[class='modal-footer']").click()
driver.close()