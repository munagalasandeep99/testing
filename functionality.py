import time
import re

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Test():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.snapdeal.com/")

        search = driver.find_element(By.ID, "inputValEnter")
        search.click()
        search.send_keys("bag")
        search_button = driver.find_element(By.CLASS_NAME,"searchTextSpan")
        search_button.click()
        time.sleep(1)
        minus = driver.find_element(By.CSS_SELECTOR,".node-toggle.sd-icon.node-open.sd-icon-minus[data-show-div='#js-1031-nav']")
        minus.click()
        time.sleep(1)
        current_url = driver.current_url
        expected_url =  "https://www.snapdeal.com/search?keyword=bag&sort=rlvncy"
        if current_url == expected_url:
            print("Test passed")
        else:
            print(f"Test failed. Expected URL: {expected_url}, but got: {current_url}")
        parent_handle = driver.current_window_handle
        low_range = driver.find_element(By.NAME, "fromVal")
        low_range.click()
        low_range.clear()
        low_range.send_keys("600")
        high_range = driver.find_element(By.NAME, "toVal")
        high_range.click()
        high_range.clear()
        high_range.send_keys("1000")
        go = driver.find_element(By.CSS_SELECTOR,"#content_wrapper > div.col-xs-24.reset-padding.marT22 > div.col-xs-5.reset-padding > div > div.left-wrapper > div.comp-left-filter > div:nth-child(3) > div.filter-content > div > div.price-go-arrow.btn.btn-line.btn-theme-secondary")
        go.click()
        time.sleep(2)
        price_element = driver.find_element(By.CSS_SELECTOR, "#display-price-647490383534")

        # Assign the text from price_element to price_text
        price_text = price_element.text

        # Use regular expressions to find all sequences of digits in the string
        numbers = re.findall(r'\d+', price_text)

        # Convert the first found number to integer
        price_number = int(numbers[0]) if numbers else None

        print(price_number)
        if 500 <= price_number <= 1000:
            print(f"Test Passed: Price {price_number} is within the range 500 to 1000.")
        else:
            print(f"Test Failed: Price {price_number} is not within the range 500 to 1000.")
        price_element.click()
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                item_url = driver.current_url
                print(item_url)
                add = driver.find_element(By.ID, "add-cart-button-id")
                add.click()
                break
        driver.switch_to.window(parent_handle)
        cart_element = driver.find_element(By.CLASS_NAME,"cartInner")
        cart_element.click()
        time.sleep(3)
        checking_element = driver.find_element(By.CLASS_NAME, "item-name")
        checking_element.click()
        urls = driver.current_url
        if urls != item_url:
            print("Test Passed:added succesfully")









x = Test()
x.test()
