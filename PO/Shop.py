import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from BrowserUtils.BrowserUtils import BrowserUtils
from PO.CheckOut_Confirm import CheckOut_Confirm


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.laptop_sec_click = (By.LINK_TEXT, "Laptops")
        self.laptop_list = (By.XPATH, "//div[@class = 'card h-100']")
        self.laptop_name= (By.XPATH, "div/h4/a")
        self.add_to_cart = (By.LINK_TEXT, "Add to cart")
        self.cart_click = (By.LINK_TEXT, "Cart")
        self.items_check_inCart = (By.XPATH, "//tbody/tr")
        self.remove_same_multiple_products = (By.XPATH, "td/a")
        self.placeOrder = (By.XPATH, "//*[text()='Place Order']")
        #hi
#y=this is new


    def product_add_to_cart(self,product_name):
        self.driver.find_element(*self.laptop_sec_click).click()
        time.sleep(2)
        laptops = self.driver.find_elements(*self.laptop_list)
        for laptop in laptops:
            lap_name = laptop.find_element(*self.laptop_name).text
            print(lap_name)
            if lap_name == product_name:
                laptop.find_element(*self.laptop_name).click()
                break

        self.driver.find_element(*self.add_to_cart).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        self.driver.find_element(*self.cart_click).click()
        no_products = self.driver.find_elements(*self.items_check_inCart )
        print(len(no_products))
        for no_product in no_products:
            if len(no_products) > 1:
                no_product.find_element(*self.remove_same_multiple_products ).click()
        self.driver.find_element(*self.placeOrder).click()
        checkOut_confirm = CheckOut_Confirm(self.driver)
        return checkOut_confirm