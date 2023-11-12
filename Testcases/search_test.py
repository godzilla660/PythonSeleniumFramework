import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter:
    def test_search(self):
        # pop_up = self.driver.wait.until(
        #     EC.element_to_be_clickable((By.XPATH, "//*[@id='themeSnipe']/div/div/div[1]/button")))
        # pop_up.click()

        #Departure City Input
        depart_city = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        depart_city.click()
        depart_city.clear()
        depart_city.send_keys("Ba")

        search_autocomplete = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//*[@id='BE_flight_form_wrapper']/div[1]/div[2]/ul/li[1]/ul/li[1]/div/div/ul/div/div")))
        for result in search_autocomplete:
            if result.text == "Bangalore":
                result.click()
                break

        #Arrival City Input
        arrival_city = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='BE_flight_arrival_city']")))
        arrival_city.click()
        arrival_city.clear()
        arrival_city.send_keys("New")

        search_autocomplete2 = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//*[@id='BE_flight_form_wrapper']/div[1]/div[2]/ul/li[1]/ul/li[3]/div/div/ul/div/div/div")))
        for result in search_autocomplete2:
            if result.text == "New Delhi (DEL)":
                result.click()
                break

        # search_flights = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']")))
        # search_flights.click()
