import logging
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils

FILTER_BY_1_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
FILTER_BY_2_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
FILTER_BY_NON_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
SEARCH_FLIGHT_RESULTS = "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]"


class SearchFlightResults(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_filter_by_one_stop_icon(self):
        return self.driver.find_element(By.XPATH, FILTER_BY_1_STOP_ICON)

    def get_filter_by_two_stop_icon(self):
        return self.driver.find_element(By.XPATH, FILTER_BY_2_STOP_ICON)

    def get_filter_by_non_stop_icon(self):
        return self.driver.find_element(By.XPATH, FILTER_BY_NON_STOP_ICON)

    def get_search_flight_result(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, SEARCH_FLIGHT_RESULTS)

    def filter_flights_by_stop(self, by_stop):
        options = {
            "1 Stop": (self.get_filter_by_one_stop_icon, "Selected flights with 1 stop"),
            "2 Stop": (self.get_filter_by_two_stop_icon, "Selected flights with 2 stop"),
            "Non Stop": (self.get_filter_by_non_stop_icon, "Selected non stop flight")
        }

        if by_stop in options:
            element_getter, message = options[by_stop]
            element = element_getter()
            ActionChains(self.driver).move_to_element(element).click().perform()
            self.log.warning(message)
            time.sleep(2)
        else:
            print("Please provide a valid filter option")


