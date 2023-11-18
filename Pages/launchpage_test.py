from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver

class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//*[@id='BE_flight_arrival_city']"
    SEARCH_FLIGHTS_BUTTON = "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']"
    def get_depart_from_location(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def fill_depart_location(self, departlocation):
        self.get_depart_from_location().click()
        self.get_depart_from_location().send_keys(departlocation)
        self.get_depart_from_location().send_keys(Keys.ENTER)

    def get_going_to_location(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)
    def fill_going_to_location(self, goingtolocation):
        self.get_going_to_location().click()
        self.get_going_to_location().send_keys(goingtolocation)
        self.get_going_to_location().send_keys(Keys.ENTER)

    #simplifying testcase searchflights to one line
    def search_flights(self, departlocation, goingtolocation):
        self.fill_depart_location(departlocation)
        self.fill_going_to_location(goingtolocation)

    def get_search_flights_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SEARCH_FLIGHTS_BUTTON)


    #click on search flights button
    def click_on_search_flights_button(self):
        self.get_search_flights_button().click()

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