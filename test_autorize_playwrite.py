from page.Locators import LoginPageLocator
from page.Login_page import LoginPage
from page.json_page import CreduForWatchdog

def test_login_in_watchdoge(browser):
        link = "https://iiot.ekfgroup.com/auth"
        login_page = LoginPage(browser)
        login_page.open(link)
        login_page.enter_login(CreduForWatchdog.email)
        login_page.enter_password(CreduForWatchdog.password)
        login_page.click_login_button()
        login_page.check_visible_selector(LoginPageLocator.LOCATOR_EKF)
        assert login_page.is_check_success()