from selenium.webdriver.common.by import By

from BrowserUtils.BrowserUtils import BrowserUtils
from PO.Shop import ShopPage


class LoginPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.login_click = (By.ID, "login2")
        self.username_input = (By.ID, "loginusername")
        self.user_password = (By.ID, "loginpassword")
        self.login_submit = (By.XPATH, "//button[@onclick='logIn()']")


    def login(self,username,password):
        self.driver.find_element(*self.login_click).click()
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.user_password ).send_keys(password)
        self.driver.find_element(*self.login_submit).click()
        shop_page = ShopPage(self.driver)
        return shop_page