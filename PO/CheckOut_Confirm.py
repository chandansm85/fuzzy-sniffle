from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from BrowserUtils.BrowserUtils import BrowserUtils


class CheckOut_Confirm(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.name_input = (By.ID, "name")
        self.country = (By.ID, "country")
        self.city = (By.ID, "city")
        self.CC = (By.ID, "card")
        self.month = (By.ID, "month")
        self.year = (By.ID, "year")
        self.purchase_click = (By.XPATH, "//*[text()='Purchase']")
        self.success_msg = (By.XPATH, "//div/h2[text()='Thank you for your purchase!']")
        self.Ok_click = (By.XPATH, "//*[text()='OK']")


    def checkout_confirm(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(locator))
        self.driver.find_element(*self.name_input ).send_keys("Chandan")
        self.driver.find_element(*self.country).send_keys("India")
        self.driver.find_element(*self.city).send_keys("Shivamogga")
        self.driver.find_element(*self.CC ).send_keys("1234")
        self.driver.find_element(*self.month).send_keys("April")
        self.driver.find_element(*self.year).send_keys("2026")
        self.driver.find_element(*self.purchase_click).click()
        msg = self.driver.find_element(*self.success_msg).text
        assert "Thank you" in msg
        self.driver.find_element(*self.Ok_click).click()