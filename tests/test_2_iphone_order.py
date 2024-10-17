import logging
from time import sleep

from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.front_page import FrontPage
from test_data.constants import WELLCOME_TEXT
from test_functions.catalog_functions import cheaper_sorting, add_to_cart, wait_for_sorting, expensive_sorting, \
    go_to_cart, cart_counting
from test_functions.cart_functions import remove_from_cart, accept_remove
from test_functions.front_functions import search_product

logger = logging.getLogger(__name__)


def test_iphone_order(driver):
    front_page = FrontPage(driver)
    front_page.load()
    search_product(driver)
    cheaper_sorting(driver)
    wait_for_sorting()
    add_to_cart(driver)

    catalog_page = CatalogPage(driver)
    confirm = catalog_page.confirmation_popup()

    assert confirm, "Сообщение о добавлении товара в корзину не найдено - ERROR!"
    logger.info("Товар успешно добавлен в корзину - OK!")
    confirm = None

    expensive_sorting(driver)
    wait_for_sorting()
    add_to_cart(driver)

    confirm = catalog_page.confirmation_popup()

    assert confirm, "Сообщение о добавлении товара в корзину не найдено - ERROR!"
    logger.info("Товар успешно добавлен в корзину - OK!")
    confirm = None

    go_to_cart(driver)

    assert cart_counting(driver) == 2, "Количество товаров не равно 2 - ERROR!"
    logging.info('Количество товаров в корзине равно 2 - ОК!')

    remove_from_cart(driver)
    accept_remove(driver)

    cart_page = CartPage(driver)
    text = cart_page.wellcome_banner()
    assert text == WELLCOME_TEXT, "Текст приветствия не найден - ERROR!"
    logging.info('Текст приветствия найден, корзина пуста - ОК!')

    sleep(3)  # Для визуализации очистки корзины, в рабочих проектах не используется
