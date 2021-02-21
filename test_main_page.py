from pages.main_page import MainPage
from pages.login_page import LoginPage
from time import sleep
def test_guest_can_go_to_login_page_and_test_guest_can_see_authorization_form(browser):
    link="http://selenium1py.pythonanywhere.com/"
    page=MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page=LoginPage(browser,browser.current_url)
    login_page.should_be_login_page()
