from pages.product_page import ProductPage
import pytest
@pytest.mark.skip
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

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
    product_page=ProductPage(browser,link)
    product_page.open()
    product_page.press_to_add_basket()
    product_page.should_not_be_success_message()
def test_guest_cant_see_success_message(browser, link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
    product_page=ProductPage(browser,link)
    product_page.open()
    product_page.should_not_be_success_message()
def test_message_disappeared_after_adding_product_to_basket(browser,link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
    product_page=ProductPage(browser,link)
    product_page.open()
    product_page.press_to_add_basket()
    product_page.should_dissapear_of_success_message()