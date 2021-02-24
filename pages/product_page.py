from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def press_to_add_basket(self):
        btn_add=self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add.click()
    def should_be_product_in_basket(self):
        product_name=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_messages_after_add=self.browser.find_element(
                    *ProductPageLocators.PRODUCT_NAME_IN_MESSAGES_AFTER_ADD).text
        assert product_name == product_name_in_messages_after_add,f"Product\
                {product_name} isn't Product {product_name_in_messages_after_add}"
    def should_be_price_in_basket_equal_price_product(self):
        product_price=float(self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.split()[0].replace(",",".").replace("\xa3",""))
        basket_price=float(self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text.split()[0].replace(",",".").replace("\xa3",""))
        assert product_price == basket_price,"Price product {product_price} isn't equal basket price {basket_price}"
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), \
           "Success message is presented, but should not be"
    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), \
               f"Message on ProductPage (CSS_SELECTOR- {ProductPageLocators.SUCCESS_MESSAGES[1]}) did not disappear"
