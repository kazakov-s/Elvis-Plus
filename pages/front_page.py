from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from test_data.constants import TEST_URL
from test_data.locators import SEARCH_FIELD, SEARCH_BUTTON, CONFIRMATION_POPUP


class FrontPage:
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(TEST_URL)

    def search_field(self):
        return WebDriverWait(self.browser, timeout=2, poll_frequency=0.5,
                             ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
            EC.element_to_be_clickable(SEARCH_FIELD)
        )

    def search_button(self):
        return WebDriverWait(self.browser, timeout=2, poll_frequency=0.5,
                             ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
            EC.element_to_be_clickable(SEARCH_BUTTON)
        )