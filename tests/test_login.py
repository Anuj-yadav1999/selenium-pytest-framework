from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_successful_login(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "Products" in inventory_page.get_title()
