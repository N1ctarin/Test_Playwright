from playwright.sync_api import Page
from page.Locators import DevicesPageLocator

class DevicePage:
    def __init__(self, page: Page):
        self.page = page

    def click_devices_in_project(self):
        self.page.wait_for_selector('text="Устройства"', timeout=3000)
        self.page.click('text="Устройства"')

    def check_folder_tags(self):
        self.page.wait_for_selector(DevicesPageLocator.FOLDER_PROJECT_TAGS, timeout=3000)
        return self.page.is_visible(DevicesPageLocator.FOLDER_PROJECT_TAGS)