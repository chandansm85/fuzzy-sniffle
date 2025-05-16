import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PO.LoginPage import LoginPage
from Tests.conftest import browser_code

file_path = '../data/test_booking.json'
with open(file_path, 'r') as f:
    test_data = json.load(f)
    test_list = test_data["data"]
@pytest.mark.parametrize("test_list_item", test_list)

def test_end2end(browser_code, test_list_item):
    driver =  browser_code
    login_page = LoginPage(driver)
    print(login_page.get_title())
    shop_page = login_page.login(test_list_item["user_name"],test_list_item["user_password"])
    print(shop_page.get_title())
    time.sleep(2)
    checkOut_confirm = shop_page.product_add_to_cart(test_list_item["device_buy"])
    print(checkOut_confirm.get_title())
    time.sleep(2)
    wait_locator = (By.ID, "totalm")
    checkOut_confirm.checkout_confirm(wait_locator)








