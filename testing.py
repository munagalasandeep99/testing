import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("driver_init")
class TestSnapdeal:

    def test_search_bag(self):
        self.driver.get("https://www.snapdeal.com/")
        search = self.driver.find_element(By.ID, "inputValEnter")
        search.click()
        search.send_keys("bag")
        search_button = self.driver.find_element(By.CLASS_NAME, "searchTextSpan")
        search_button.click()

        WebDriverWait(self.driver, 10).until(EC.url_contains("keyword=bag&sort=rlvncy"))
        assert self.driver.current_url == "https://www.snapdeal.com/search?keyword=bag&sort=rlvncy", "URL does not match expected search URL."

    def test_price_filter(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".node-toggle.sd-icon.node-open.sd-icon-minus[data-show-div='#js-1031-nav']"))).click()

        low_range = self.driver.find_element(By.NAME, "fromVal")
        low_range.click()
        low_range.clear()
        low_range.send_keys("600")

        high_range = self.driver.find_element(By.NAME, "toVal")
        high_range.click()
        high_range.clear()
        high_range.send_keys("1000")

        go_button = self.driver.find_element(By.CSS_SELECTOR, ".price-go-arrow")
        go_button.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#display-price-647490383534")))
        price_element = self.driver.find_element(By.CSS_SELECTOR, "#display-price-647490383534")
        price_text = price_element.text
        price_number = int(re.search(r'\d+', price_text).group()) if re.search(r'\d+', price_text) else None
        assert 600 <= price_number <= 1000, f"Price {price_number} is not within the range 600 to 1000."

"""    def test_add_to_cart_and_check(self):
        parent_handle = self.driver.current_window_handle
        price_element = self.driver.find_element(By.CSS_SELECTOR, "#display-price-647490383534")
        price_element.click()

        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                add_button = self.driver.find_element(By.ID, "add-cart-button-id")
                add_button.click()
                break

        self.driver.switch_to.window(parent_handle)
        cart_element = self.driver.find_element(By.CLASS_NAME, "cartInner")
        cart_element.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "item-name")))
        checking_element = self.driver.find_element(By.CLASS_NAME, "item-name")
        checking_element.click()

        item_url = self.driver.current_url
        assert item_url != parent_handle, "Item was not added successfully to the cart."
"""
