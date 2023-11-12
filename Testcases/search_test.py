import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter:
    def test_search(self):

        pop_up = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pop']/div/section/button/svg/use")))
        pop_up.click()

        depart_from = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Official Stores']")))
        depart_from.click()
        #depart_from.send_keys("New Delhi")

        arrival_city = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@ng-if='!submitted']")))
        arrival_city.click()
        #arrival_city.send_keys("New York")

        # search_autocomplete = self.wait.until(EC.presence_of_all_elements_located(
        #     (By.XPATH, "//*[@id='BE_flight_form_wrapper']/div[1]/div[2]/ul/li[1]/ul/li[3]/div/div/ul")))
        # for result in search_autocomplete:
        #     if result.text == "New York":
        #         result.click()
        #         break
