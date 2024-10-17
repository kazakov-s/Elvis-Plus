import pytest

from selenium import webdriver

from test_data.constants import TEST_URL


@pytest.fixture(scope='function')
def driver(request):

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()


