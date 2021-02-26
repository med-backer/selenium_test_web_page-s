from selenium.webdriver.common.by import By

class BasePageLocators():
    BASKET_BTN=(By.CSS_SELECTOR,".basket-mini .btn-default:nth-child(1)")
    LOGIN_LINK_BTN=(By.CSS_SELECTOR,"#login_link")
    LOGIN_LINK_BTN_INVALID=(By.CSS_SELECTOR,"#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class MainPageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR,"#login_link")

class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR,"form#login_form")
    REGISTER_FORM=(By.CSS_SELECTOR,"form#register_form")
    REGISTER_LOGIN_INPUT=(By.CSS_SELECTOR,"input[name='registration-email']")
    REGISTER_PASSWORD_INPUT=(By.CSS_SELECTOR,"input[name='registration-password1']")
    REGISTER_PASSWORD_REPEAT_INPUT=(By.CSS_SELECTOR,"input[name='registration-password2']")
    REGISTER_SUBMIT_BTN=(By.CSS_SELECTOR,"button[name='registration_submit']")
class ProductPageLocators():
    BTN_ADD_TO_BASKET=(By.CSS_SELECTOR,"button.btn-add-to-basket")
    PRODUCT_NAME=(By.CSS_SELECTOR,".product_page h1")
    PRODUCT_NAME_IN_MESSAGES_AFTER_ADD=(By.CSS_SELECTOR,"div#messages .alert:nth-child(1) strong")
    PRODUCT_PRICE=(By.CSS_SELECTOR,"table tr:nth-child(4) td")
    BASKET_PRICE=(By.CSS_SELECTOR,".alert-info .alertinner strong")
    SUCCESS_MESSAGES=(By.CSS_SELECTOR,".alert-success")

class BasketPageLocators():
    PRODUCT_IN_BASKET_PAGE=(By.CSS_SELECTOR,".basket-items")
    TEXT_SHOPPING_CART_IS_EMPTY=(By.CSS_SELECTOR,"div#content_inner p")
