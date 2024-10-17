from selenium.webdriver.common.by import By

SEARCH_FIELD = (By.XPATH, '//input[@id="header-search"]')
SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
GRID_VIEW = (By.XPATH, '//input[@value="grid"]')
CHEAPER_SORT = (By.XPATH, '//button[@data-autotest-id="aprice"]')
EXPENSIVE_SORT = (By.XPATH, '//button[@data-autotest-id="dprice"]')
ADD_TO_CART_BTN = (By.XPATH, '//div[@data-zone-name="cartButton"]')
CONFIRMATION_POPUP = (By.XPATH, '//div[@data-auto="notification"]')
CART_ICON = (By.XPATH, '//div[@id="CART_ENTRY_POINT_ANCHOR"]')
REMOVE_FROM_CART_BTN = (By.XPATH, '//button[@data-auto="deleteChosenButton"]')
ACCEPT_BTN = (By.XPATH, '//button[@data-auto="checkout-popup-submit"]')
WELLCOME_BANNER = (By.XPATH, '//span[text()="Войдите в аккаунт"]')
