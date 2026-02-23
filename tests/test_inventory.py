from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_item_to_cart()
    cart_count = inventory_page.get_text((By.CLASS_NAME, "shopping_cart_badge"))
    assert cart_count == "1"

