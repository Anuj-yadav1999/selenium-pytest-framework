# Adding a fixture to initialize and quit the WebDriver for each test

import pytest
from utils.driver_factory import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

