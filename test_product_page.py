from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
import pytest
import time
@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                    marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser,link):
    product_page=ProductPage(browser,link)
    product_page.open()
    product_page.press_to_add_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_in_basket()
    product_page.should_be_price_in_basket_equal_price_product()
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
    product_page=ProductPage(browser,link)
    product_page.open()
    product_page.press_to_add_basket()
    product_page.should_not_be_success_message()
def test_guest_cant_see_success_message(browser, link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
    product_page=ProductPage(browser,link)
    product_page.open()
    product_page.should_not_be_success_message()
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser,link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
    product_page=ProductPage(browser,link)
    product_page.open()
    product_page.press_to_add_basket()
    product_page.should_dissapear_of_success_message()
def test_guest_should_see_login_link_on_product_page(browser):
    link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page=ProductPage(browser,link)
    page.open()
    page.should_be_login_link()
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page=ProductPage(browser,link)
    page.open()
    page.should_be_login_link()
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page=ProductPage(browser,link)
    page.open()
    page.go_to_basket_page()
    basket_page=BasketPage(browser,browser.current_url)
    basket_page.should_not_be_product()
    basket_page.should_be_text_that_the_shopping_cart_is_empty()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link="http://selenium1py.pythonanywhere.com"
        main_page=MainPage(browser,link)
        user_email=str(time.time()) + "@fakemail.org"
        user_password=str(time.time())[0:10]
        main_page.open()
        main_page.go_to_login_page()
        login_page=LoginPage(browser,link)
        login_page.register_new_user(user_email,user_password)
        login_page.should_be_authorized_user()
    def test_user_cant_see_success_message(self,browser, link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
        product_page=ProductPage(browser,link)
        product_page.open()
        product_page.should_not_be_success_message()
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser,link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
        product_page=ProductPage(browser,link)
        product_page.open()
        product_page.press_to_add_basket()
        product_page.should_be_product_in_basket()
        product_page.should_be_price_in_basket_equal_price_product()
        
