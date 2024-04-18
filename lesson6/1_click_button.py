# перейти на сайт;
# нажать на синюю кнопку;
# дождаться появления зеленой плашки;
# получить текст с плашки и вывести его в терминал.# перейти на сайт;

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# перейти на сайт;
# нажать на синюю кнопку;
# дождаться появления зеленой плашки;
# получить текст с плашки и вывести его в терминал.# перейти на сайт;

driver.implicitly_wait(20)
driver.get("http://www.uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

green = driver.find_element(By.CSS_SELECTOR, "#content")
txt = green.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt)

driver.quit()