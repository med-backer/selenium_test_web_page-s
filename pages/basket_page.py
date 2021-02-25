from pages.locators import BasketPageLocators
from pages.base_page import BasePage

class BasketPage(BasePage):
    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET_PAGE),\
               "there are products in the cart"
    def should_be_text_that_the_shopping_cart_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_SHOPPING_CART_IS_EMPTY),\
               "error in the shopping cart there is no text indicating that the shopping cart is empty"
