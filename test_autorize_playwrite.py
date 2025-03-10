from page.Locators import LoginPageLocator
from page.json_page import DateForTesting
from page.Login_page import LoginPage
from page.json_page import CreduForWatchdog
from page.Main_page import MainPage
from page.Device_page import DevicePage
from page.Scripts_page import ScriptsPage
import pytest

class TestSuite:
        def test_login_in_stage(self, browser):
                link = "https://ekf-connect-industry.stage.iot.ekfgroup.com/auth"
                login_page = LoginPage(browser)
                login_page.open(link)
                login_page.enter_login(CreduForWatchdog.email)
                login_page.enter_password(CreduForWatchdog.password)
                login_page.click_login_button()
                login_page.check_visible_selector(LoginPageLocator.LOCATOR_EKF)
                assert login_page.is_check_success()

        def test_create_new_project(self, browser):
                main_page = MainPage(browser)
                main_page.push_button_creat_new_project()
                main_page.enter_name_new_project(DateForTesting.name_new_project)
                main_page.enter_description_new_project(DateForTesting.description_new_project)
                main_page.push_button_save_new_project()
                assert main_page.check_project(DateForTesting.name_new_project)

        def test_check_folder_tags(self, browser):
                device_page = DevicePage(browser)
                main_page = MainPage(browser)
                main_page.search_and_click_project(DateForTesting.name_new_project)
                device_page.click_devices_in_project()
                assert device_page.check_folder_tags()

        def test_button_add_first_script(self, browser):
                script_page = ScriptsPage(browser)
                main_page = MainPage(browser)
                main_page.search_and_click_project(DateForTesting.name_new_project)
                script_page.click_scripts_in_project()
                assert script_page.check_button_add_first_script()

        @pytest.mark.xfail
        def test_delete_project(self, browser):
                main_page = MainPage(browser)
                main_page.search_and_click_project(DateForTesting.name_new_project)
                main_page.click_settings_in_project()
                main_page.click_delete_project()
                assert main_page.check_project(DateForTesting.name_new_project)




class TestovazOtladka:
        def test_login_in_stage(self, browser):
                link = "https://ekf-connect-industry.stage.iot.ekfgroup.com/auth"
                login_page = LoginPage(browser)
                login_page.open(link)
                login_page.enter_login(CreduForWatchdog.email)
                login_page.enter_password(CreduForWatchdog.password)
                login_page.click_login_button()
                login_page.check_visible_selector(LoginPageLocator.LOCATOR_EKF)
                assert login_page.is_check_success()

        def test_check_folder_tags(self, browser):
                device_page = DevicePage(browser)
                main_page = MainPage(browser)
                main_page.search_and_click_project(DateForTesting.name_new_project)
                device_page.click_devices_in_project()
                assert device_page.check_folder_tags()

        def test_button_add_first_script(self, browser):
                script_page = ScriptsPage(browser)
                main_page = MainPage(browser)
                main_page.search_and_click_project(DateForTesting.name_new_project)
                script_page.click_scripts_in_project()
                assert script_page.check_button_add_first_script()

