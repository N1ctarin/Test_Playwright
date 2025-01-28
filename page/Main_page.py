from playwright.sync_api import Page
from page.Locators import MainPageLocator
from page.json_page import DateForTesting

class MainPage:
    def __init__(self, page: Page):
        self.page = page

    def push_button_creat_new_project(self):
        self.page.click(MainPageLocator.BUTTON_CREAT_NEW_PROJECT)

    def enter_name_new_project(self):
        self.page.fill(MainPageLocator.NAME_NEW_PROJECT, DateForTesting.name_new_project)

    def enter_description_new_project(self):
        self.page.fill(MainPageLocator.DESCRIPTION_NEW_PROJECT, DateForTesting.description_new_project)

    def push_button_save_new_project(self):
        self.page.click(MainPageLocator.SAVE_NEW_PROJECT_BUTTON)

    def check_create_project(self):
        return self.page.locator(f'text={DateForTesting.name_new_project}')