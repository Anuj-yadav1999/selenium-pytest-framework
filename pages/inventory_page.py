# This file contains the InventoryPage class, which represents the inventory page of the application.

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):

    TITLE = (By.CLASS_NAME, "title")
    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")

    def get_title(self):
        return self.get_text(self.TITLE)
    
    def add_item_to_cart(self):
        self.click(self.ADD_TO_CART)

