from playwright.sync_api import Page, expect
from menu_page import MenuPage
from about_us_page import AboutusPage
from contacto_page import ContactoPage
from products_page import ProductsPage
from shopping_cart_page import ShoppingcartPage




class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/"
        