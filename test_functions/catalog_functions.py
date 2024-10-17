import logging
from time import sleep

from selenium.webdriver.common.by import By

from pages.catalog_page import CatalogPage

logger = logging.getLogger(__name__)


def set_grid_view(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.set_grid_view().click()


def scroll_to_position(driver):
    scroll = 1000
    for i in range(10):
        script = f"window.scrollTo(0, {scroll});"
        driver.execute_script(script)
        scroll += 1000
        sleep(2)


def goods_counting(driver):
    goods = driver.find_elements(By.XPATH, '//article[@data-auto="searchOrganic"]')
    goods_count = len(goods)
    return goods_count


def cheaper_sorting(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.cheaper_sort().click()


def expensive_sorting(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.expensive_sort().click()


def wait_for_sorting():
    sleep(2)


def add_to_cart(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.add_to_cart().click()


def go_to_cart(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.go_to_cart().click()
    wait_for_sorting()


def cart_counting(driver):
    goods = driver.find_elements(By.XPATH, '//div[@data-zone-name="cartSnippet"]')
    cart_count = len(goods)
    return cart_count
