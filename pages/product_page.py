from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        self.should_be_add_to_cart_button()
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.add_to_cart_button)
        add_to_cart_button.click()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.add_to_cart_button), "Add to cart button is not presented"

    def should_be_product_add_to_cart_notification(self):
        assert self.is_element_present(*ProductPageLocators.product_add_to_cart_notification), \
            "Add to cart notification is not presented"
        self.should_be_product_name_in_add_to_cart_notification()

    def should_be_product_name_in_add_to_cart_notification(self):
        product_name = self.browser.find_element(*ProductPageLocators.product_name)
        product_name_in_add_to_cart_notification = self.browser.find_element(*ProductPageLocators
                                                                             .product_name_in_add_to_cart_notification)
        assert product_name_in_add_to_cart_notification.text == product_name.text

    def should_be_cart_value_notification(self):
        assert self.is_element_present(*ProductPageLocators.cart_value_notification), \
            "Cart value notification is not presented"
        self.should_be_product_price_in_add_to_cart_notification()

    def should_be_product_price_in_add_to_cart_notification(self):
        product_price = self.browser.find_element(*ProductPageLocators.product_price)
        cart_value = self.browser.find_element(*ProductPageLocators.cart_value)
        assert cart_value.text == product_price.text
