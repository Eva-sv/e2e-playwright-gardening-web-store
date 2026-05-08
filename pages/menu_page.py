from playwright.sync_api import Page, expect

class MenuPage:
    def __init__(self, page: Page):
         self.page = page
         self.url = 'https://web-qa.dev.adalab.es'

    def open_menu_page(self):
         self.page.goto(self.url)