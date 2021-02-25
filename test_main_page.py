from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
from time import sleep
def test_guest_can_go_to_login_page_and_test_guest_can_see_authorization_form(browser):
    link="http://selenium1py.pythonanywhere.com/"
    page=MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page=LoginPage(browser,browser.current_url)
    login_page.should_be_login_page()
def test_guest_cant_see_product_in_basked_opened_from_main_page(browser):
    link="http://selenium1py.pythonanywhere.com/"
    page=MainPage(browser,link)
    page.open()
    page.go_to_basket_page()
    basket_page=BasketPage(browser,browser.current_url)
    basket_page.should_not_be_product()
    basket_page.should_be_text_that_the_shopping_cart_is_empty()
