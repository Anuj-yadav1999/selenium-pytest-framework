from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_successful_login(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "Products" in inventory_page.get_title()

def test_failed_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("invalid_user", "invalid_password")

    error_message = login_page.get_text((By.CSS_SELECTOR, ".error-message-container"))

    assert "Username and password do not match any user in this service" in error_message

