from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Перейдите на сайт
# Дождитесь загрузки всех картинок.
# Получите значение атрибута   src  у 3-й картинки.
# Выведите значение в консоль.

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
driver.maximize_window()
driver.implicitly_wait(10)

waiter = WebDriverWait(driver, 10, 0.1)

text_ = 'Done!'
waiter.until(
    EC.text_to_be_present_in_element((By.ID, "text"), text_))
       
search_area = driver.find_element(By.ID, "image-container")
search_scr = search_area.find_elements(By.CSS_SELECTOR, "img")[2].get_attribute("src")
  
print(search_scr)
  
driver.quit()