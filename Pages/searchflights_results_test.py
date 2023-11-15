import time
from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver

class SearchFlightsResults(BaseDriver):
    def __int__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def filter_flights(self):
        self.driver.find_element(By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()='1']").click()
        time.sleep()