import pytest
from Pages.launchpage_test import LaunchPage
from Utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():
    def test_search(self):
        #Departure City Input
        launch_page = LaunchPage(self.driver)
        #launch_page.depart_from("New Delhi")
        launch_page.fillDepartLocation("New Delhi")
        #Arrival City Input
        launch_page.fillGoingToLocation("New York")

        # allstops1 = launch_page.wait_for_presence_of_all_elements(By.XPATH, "")
        #
        # ut = Utils()
        # ut.assertListItems(allstops1, "1 stop")






