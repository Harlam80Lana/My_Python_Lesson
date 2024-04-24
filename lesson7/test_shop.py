from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from class_shop_page import ShopPage

def test_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
                                               
    shop_page = ShopPage(browser)                         
    shop_page.get()
    shop_page.authoriz_form()
    shop_page.login_button()

    shop_page.add_products()
    shop_page.shopping_cart_link()

    shop_page.confirmation()

    shop_page.post_send_key()
    shop_page.to_click()

    total = shop_page.time_waiter()                     
    browser.quit()

    assert total == 'Total: $58.29'