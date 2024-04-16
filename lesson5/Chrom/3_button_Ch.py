from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Клик по кнопке
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for button_click in range(5):
    driver.find_element(By.CSS_SELECTOR,"[onclick='addElement()']").click()
delete_elements = driver.find_elements(By.CSS_SELECTOR,"[class='added-manually']")
print(len(delete_elements))
sleep(1)

driver.close()