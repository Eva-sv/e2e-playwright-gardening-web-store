from playwright.sync_api import Page, expect

class ShoppingcartPage:
    def __init__(self, page: Page):
         self.page = page
         