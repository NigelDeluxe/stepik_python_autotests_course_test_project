from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.products_in_cart), \
            "Products in cart are presented, but should not be"

    def should_be_empty_cart_message(self):
        assert self.is_element_present(*BasketPageLocators.empty_cart_message), "Empty cart message is not presented"
