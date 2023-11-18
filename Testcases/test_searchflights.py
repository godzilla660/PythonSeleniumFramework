import pytest
import softest
from Pages.launchpage_test import LaunchPage
from Pages.searchflights_results_test import SearchFlightsResults
from Utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.launch_page = LaunchPage(self.driver)
        self.flight_results = SearchFlightsResults(self.driver)
        #self.Ut = Utils(self.driver)

    def test_search(self):
        self.launch_page.search_flights("New Delhi", "New York")
        self.launch_page.click_on_search_flights_button()
        #self.Ut.assertListItems(allstops1, "1 stop")

    def test_search_2(self):
        self.launch_page.search_flights("JKF", "Mumbai")
        self.launch_page.click_on_search_flights_button()
        #self.flight_results.click_filter_flights()
        #launch_page.depart_from("New Delhi")
        # launch_page.fillDepartLocation("New Delhi")
        # #Arrival City Input
        # launch_page.fillGoingToLocation("New York")

        # allstops1 = launch_page.wait_for_presence_of_all_elements(By.XPATH, "")
        #
        # ut = Utils()
        # ut.assertListItems(allstops1, "1 stop")






