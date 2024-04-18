from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Перейдите на сайт: http://uitestingplayground.com/textinput.
#Укажите в поле ввода текст SkyPro.
#Нажмите на синюю кнопку.
#Получите текст кнопки и выведите в консоль (SkyPro).

driver.implicitly_wait(20)
driver.get("http://uitestingplayground.com/textinput")
driver.maximize_window()

#search_field = "#newButtonName"  
#search_input = driver.find_element(By.CSS_SELECTOR, search_field)
#search_input.send_keys("SkyPro")
 
#waiter = WebDriverWait(driver, 10, 0.1) 
#waiter.until(
#    EC.element_to_be_clickable((By.CSS_SELECTOR, "#updatingButton"))).click() 
#txt = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
#print(txt)
                            # УПРОСТИЛА
search_field = driver.find_element(By.ID, "newButtonName")
search_field.send_keys("SkyPro")

WebDriverWait(driver, 10, 0.1).until(EC.element_to_be_clickable((By.ID, "updatingButton"))).click()
text = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text

print(text)

driver.quit()