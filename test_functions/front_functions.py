from pages.front_page import FrontPage
from test_data.constants import SEARCH_TEXT


def search_product(driver):
    front_page = FrontPage(driver)
    front_page.search_field().send_keys(SEARCH_TEXT)
    front_page.search_button().click()
