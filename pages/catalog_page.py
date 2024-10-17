from selenium.webdriver.support import expected_conditions as EC

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from test_data.locators import GRID_VIEW, CHEAPER_SORT, ADD_TO_CART_BTN, CONFIRMATION_POPUP, EXPENSIVE_SORT, CART_ICON


class CatalogPage:
    def __init__(self, browser):
        self.browser = browser

    def set_grid_view(self):
        return WebDriverWait(self.browser, timeout=3, poll_frequency=0.5,
                             ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
            EC.presence_of_element_located(GRID_VIEW)
        )

    def cheaper_sort(self):
        return WebDriverWait(self.browser, timeout=3, poll_frequency=0.5,
                             ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
            EC.presence_of_element_located(CHEAPER_SORT)
        )

    def expensive_sort(self):
        return WebDriverWait(self.browser, timeout=3, poll_frequency=0.5,
                             ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
            EC.presence_of_element_located(EXPENSIVE_SORT)
        )

    def add_to_cart(self):
        return WebDriverWait(self.browser, timeout=3, poll_frequency=0.5,
                             ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
            EC.visibility_of_element_located(ADD_TO_CART_BTN)
        )

    def confirmation_popup(self):
        try:
            WebDriverWait(self.browser, timeout=5, poll_frequency=1,
                          ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
                EC.visibility_of_element_located(CONFIRMATION_POPUP))
            return True
        except Exception:
            return False

    def go_to_cart(self):
        return WebDriverWait(self.browser, timeout=3, poll_frequency=0.5,
                             ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
            EC.visibility_of_element_located(CART_ICON)
        )

