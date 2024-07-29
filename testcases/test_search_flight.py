import pytest
import softest
from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils

# WEBSITE_URL = "https://www.yatra.com/"


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_logger()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    # def setup_method(self, method):
    #     # Ensure starting from the base URL before each test
    #     self.driver.get(WEBSITE_URL)

    def test_search_flight_one_stop(self):
        search_flight_result = self.lp.search_flights("New Delhi", "JFK", "06/08/2024")
        self.lp.page_scroll()  # To handle Dynamic Scroll
        search_flight_result.filter_flights_by_stop("1 Stop")
        all_stops_1 = search_flight_result.get_search_flight_result()
        self.log.info(f"Number of all stop flights: {len(all_stops_1)}")
        self.ut.assert_list_item_text(all_stops_1, "1 Stop")

    # def test_search_flight_two_stop(self):
    #     search_flight_result = self.lp.search_flights("New Delhi", "New York", "06/08/2024")
    #     self.lp.page_scroll()  # To handle Dynamic Scroll
    #     search_flight_result.filter_flights_by_stop("2 Stop")
    #     all_stops_1 = search_flight_result.get_search_flight_result()
    #     print(len(all_stops_1))
    #     self.ut.assert_list_item_text(all_stops_1, "2 Stop")


