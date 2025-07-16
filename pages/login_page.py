from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Expected 'login' to be in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.email_input)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.password_input)
        password_input.send_keys(password)
        repeat_password_input = self.browser.find_element(*LoginPageLocators.repeat_password_input)
        repeat_password_input.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.register_button)
        register_button.click()
