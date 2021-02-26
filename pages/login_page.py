import time
from pages.base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self,email,password):
        register_login_input=self.browser.find_element(*LoginPageLocators.REGISTER_LOGIN_INPUT)
        register_password_input=self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT)
        register_password_repeat_input=self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT_INPUT)
        register_submit_btn=self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BTN)
        register_login_input.send_keys(email)
        register_password_input.send_keys(password)
        register_password_repeat_input.send_keys(password)
        register_submit_btn.click()
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url.find("login")>-1, "Its page isnt login page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)>0,"Login form not here"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)>0,"Registor form not here"
