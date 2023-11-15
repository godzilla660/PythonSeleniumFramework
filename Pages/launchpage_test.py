from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver

class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//*[@id='BE_flight_arrival_city']"
    def getDepartFromLocation(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def fillDepartLocation(self, departlocation):
        self.getDepartFromLocation().click()
        self.getDepartFromLocation().send_keys(departlocation)
        self.getDepartFromLocation().send_keys(Keys.ENTER)

    def getGoingToLocation(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)
    def fillGoingToLocation(self, goingtolocation):
        self.getGoingToLocation().click()
        self.getGoingToLocation().send_keys(goingtolocation)
        self.getGoingToLocation().send_keys(Keys.ENTER)

    # def going_to(self, goingtolocation):
    #     #arrival_city = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='BE_flight_arrival_city']")))
    #     arrival_city = self.wait_until_element_is_clickable(By.XPATH, "//*[@id='BE_flight_arrival_city']")
    #     arrival_city.click()
    #     arrival_city.clear()
    #     arrival_city.send_keys(goingtolocation)

        # search_results = self.wait_for_presence_of_all_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        #
        # for result in search_results:
        #     if result.text == "New York":
        #         result.click()
        #         break