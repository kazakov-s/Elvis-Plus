from selenium.webdriver.support import expected_conditions as EC

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from test_data.locators import REMOVE_FROM_CART_BTN, ACCEPT_BTN, WELLCOME_BANNER


class CartPage:
    def __init__(self, browser):
        self.browser = browser

    def remove_from_cart(self):
        return WebDriverWait(self.browser, timeout=3, poll_frequency=0.5,
                             ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
            EC.visibility_of_element_located(REMOVE_FROM_CART_BTN)
        )

    def accept_btn(self):
        return WebDriverWait(self.browser, timeout=3, poll_frequency=0.5,
                             ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
            EC.element_to_be_clickable(ACCEPT_BTN)
        )

    def wellcome_banner(self):
        try:
            text = WebDriverWait(self.browser, timeout=5, poll_frequency=1,
                          ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
                EC.visibility_of_element_located(WELLCOME_BANNER)).text
            return text
        except Exception:
            return None
