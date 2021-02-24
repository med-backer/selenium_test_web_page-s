from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR,"#login_link")

class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR,"form#login_form")
    REGISTER_FORM=(By.CSS_SELECTOR,"form#register_form")
    
class ProductPageLocators():
    BTN_ADD_TO_BASKET=(By.CSS_SELECTOR,"button.btn-add-to-basket")
    PRODUCT_NAME=(By.CSS_SELECTOR,".product_page h1")
    PRODUCT_NAME_IN_MESSAGES_AFTER_ADD=(By.CSS_SELECTOR,"div#messages .alert:nth-child(1) strong")
    PRODUCT_PRICE=(By.CSS_SELECTOR,"table tr:nth-child(4) td")
    BASKET_PRICE=(By.CSS_SELECTOR,".alert-info .alertinner strong")
    SUCCESS_MESSAGES=(By.CSS_SELECTOR,".alert-success")
    
