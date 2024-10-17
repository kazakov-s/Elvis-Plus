import logging
from time import sleep

from selenium.webdriver.common.by import By

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from test_functions.catalog_functions import wait_for_sorting

logger = logging.getLogger(__name__)


def remove_from_cart(driver):
    cart_page = CartPage(driver)
    cart_page.remove_from_cart().click()
    wait_for_sorting()


def accept_remove(driver):
    cart_page = CartPage(driver)
    cart_page.accept_btn().click()
