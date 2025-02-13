from time import sleep

from playwright.sync_api import Page
from page.Locators import MainPageLocator

class MainPage:
    def __init__(self, page: Page):
        self.page = page

    def push_button_creat_new_project(self):
        self.page.click(MainPageLocator.BUTTON_CREAT_NEW_PROJECT)

    def enter_name_new_project(self, name):
        self.page.fill(MainPageLocator.NAME_NEW_PROJECT, name)

    def enter_description_new_project(self, descriptions):
        self.page.fill(MainPageLocator.DESCRIPTION_NEW_PROJECT, descriptions)

    def push_button_save_new_project(self):
        self.page.click(MainPageLocator.SAVE_NEW_PROJECT_BUTTON)

    def check_project(self, name):
        return self.page.locator(f'text={name}')

    def search_and_click_project(self, name):
        self.page.click(f'text={name}')

    def click_settings_in_project(self):
        self.page.wait_for_selector('text="Настройки"', timeout=3000)
        self.page.click('text="Настройки"')

    def click_delete_project(self):
        self.page.wait_for_selector('text=" Удалить проект"', timeout=3000)
        self.page.click('text=" Удалить проект"')
        self.page.click(MainPageLocator.DELETE_BUTTON)
        self.page.bring_to_front()
