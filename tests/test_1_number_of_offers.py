import logging

from pages.front_page import FrontPage
from test_functions.catalog_functions import set_grid_view, scroll_to_position, goods_counting
from test_functions.front_functions import search_product

logger = logging.getLogger(__name__)


def test_iphone_15_number_of_offers(driver):
    front_page = FrontPage(driver)
    front_page.load()
    search_product(driver)
    set_grid_view(driver)
    scroll_to_position(driver)
    assert goods_counting(driver) > 50, "Количество товаров меньше 50"
    logging.info('Количество предложений iPhone 15 Pro больше 50-ти - ОК!')
