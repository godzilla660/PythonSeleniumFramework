from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver

class SearchFlightsResults(BaseDriver):
    def __int__(self, driver):
        super().__init__(driver)
        self.driver = driver


    FILTER_FLIGHTS = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    def get_filter_flights(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_FLIGHTS)

    def click_filter_flights(self):
        self.get_filter_flights().click()

    # def filter_flights(self):
    #     self.driver.find_element(By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()='1']").click()
    #     time.sleep()

