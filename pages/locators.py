from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    login_form = (By.CSS_SELECTOR, "#login_form")
    register_form = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    add_to_cart_button = (By.CSS_SELECTOR, ".btn-add-to-basket")
    product_name = (By.CSS_SELECTOR, ".product_main > h1")
    product_price = (By.CSS_SELECTOR, ".product_main .price_color")
    product_add_to_cart_notification = (By.CSS_SELECTOR, "#messages > div:first-child")
    product_name_in_add_to_cart_notification = (By.CSS_SELECTOR, "#messages > div:first-child strong")
    cart_value_notification = (By.CSS_SELECTOR, "#messages > div:last-child")
    cart_value = (By.CSS_SELECTOR, "#messages > div:last-child strong")


class BasePageLocators:
    login_link = (By.CSS_SELECTOR, "#login_link")
    cart_link = (By.CSS_SELECTOR, ".btn-group > a")


class BasketPageLocators:
    products_in_cart = (By.CSS_SELECTOR, ".basket-title")
    empty_cart_message = (By.CSS_SELECTOR, "#content_inner > p")
