from selenium import webdriver
from my_midgets.midget import Midget
import time

class RestaurantMidget(Midget):

    RESERVE_BASE_URL = "https://reserve.com/"
    carbone_url = RESERVE_BASE_URL + "r/carbone-new-york"

    # class constants
    GUEST_NUM_CLASS = "bcfoPudn"
    CALENDAR_CLASS = "_9sbLNGMr"
    NEXT_MONTH_CLASS = "b2Wlr7gA"
    DATE_CLASS = "_73peZ3mZ"
    DATE_ENABLED_CLASS = "_475o170v"
    TIME_AVAILABLE_CLASS = "dUc7wYir"
    TIME_CLASS="_1fnMkC-s"

    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def check_reservation(self, restaurant, guests, time, latest=True):
        url = "{}/r/{}".format(self.RESERVE_BASE_URL, restaurant)
        self.driver.get(url)

        self._select_num_guests(guests)
        self._select_time(time)

        available = self._get_available_dates()
        if available:
            available[-1].click()
            return self.driver.find_element_by_class_name(self.CALENDAR_CLASS).text
        return None

    def make_future_reservation(self, restaurant, guests, time):
        url = "{}/r/{}".format(self.RESERVE_BASE_URL, restaurant)
        self.driver.get(url)

        self._select_num_guests(guests)
        self._select_time(time)

    def _select_num_guests(self, guest_num):
        # Get guest number element
        self.driver.find_element_by_class_name(self.GUEST_NUM_CLASS).click()
        self.driver.find_element_by_xpath("//*[contains(text(), '{} guests')]".format(guest_num)).click()

    def _select_time(self, desired_time, pm=True):
        self.driver.find_element_by_class_name(self.TIME_CLASS).click()
        self.driver.find_element_by_xpath("//*[contains(text(), '{} {}')]".format(desired_time, "PM" if pm else "AM")).click()

    def _get_available_dates(self):
        # Get calendar element
        self.driver.find_element_by_class_name(self.CALENDAR_CLASS).click()
        self.driver.implicitly_wait(5)
        time.sleep(1)
        try:
            self.driver.find_element_by_class_name(self.NEXT_MONTH_CLASS).click()
            self.driver.implicitly_wait(5)
        except Exception as e:
            print(e)

        enabled_dates = self.driver.find_elements_by_class_name(self.DATE_ENABLED_CLASS)
        available_dates = self.driver.find_elements_by_class_name(self.TIME_AVAILABLE_CLASS)
        return available_dates

