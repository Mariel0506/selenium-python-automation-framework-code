import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.search_flights_results_page import SearchFlightResults
from utilities.utils import Utils

DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
GOING_TO_RESULT_LIST = "//div[@class='viewport']//div[1]/li"
SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
SEARCH_BUTTON = "//input[@value='Search Flights']"


class LaunchPage(BaseDriver):
    log = Utils.custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_depart_from_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, DEPART_FROM_FIELD)

    def get_going_to_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, GOING_TO_FIELD)

    def get_going_result_list(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, GOING_TO_RESULT_LIST)

    def get_departure_date_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, SELECT_DATE_FIELD)

    def get_all_dates_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, ALL_DATES)

    def get_search_button(self):
        return self.driver.find_element(By.XPATH, SEARCH_BUTTON)

    def enter_depart_from_location(self, depart_location):
        self.get_depart_from_field().click()
        self.get_depart_from_field().send_keys(depart_location)
        self.get_depart_from_field().send_keys(Keys.ENTER)

    def enter_going_to_location(self, going_to_location):
        self.get_going_to_field().click()
        self.log.info("Clicked on going to")
        time.sleep(2)
        self.get_going_to_field().send_keys(going_to_location)
        self.log.info("Typed text into going to field successfully")
        time.sleep(2)
        search_results = self.get_going_result_list()
        for result in search_results:
            # self.log.info(f"RESULT: {result.text}")
            if going_to_location in result.text:
                result.click()
                break

    def enter_departure_date(self, departure_date):
        self.get_departure_date_field().click()
        all_dates = self.get_all_dates_field().find_elements(By.XPATH, ALL_DATES)
        for date in all_dates:
            if date.get_attribute("data-date") == departure_date:
                date.click()
                break

    def click_search_button(self):
        self.get_search_button().click()
        time.sleep(5)

    def search_flights(self, depart_location, going_to_location, departure_date):
        self.enter_depart_from_location(depart_location)
        time.sleep(1)
        self.enter_going_to_location(going_to_location)
        time.sleep(1)
        self.enter_departure_date(departure_date)
        self.click_search_button()
        search_flights_result = SearchFlightResults(self.driver)
        return search_flights_result





