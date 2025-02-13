from playwright.sync_api import Page

class ScriptsPage:
    def __init__(self, page: Page):
        self.page = page

    def click_scripts_in_project(self):
        self.page.wait_for_selector('text="Скрипты"', timeout=3000)
        self.page.click('text="Скрипты"')

    def check_button_add_first_script(self):
        self.page.wait_for_selector('text="Добавить"', timeout=3000)
        return self.page.is_visible('text="Добавить"')