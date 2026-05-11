
from playwright.sync_api import Page, expect



class ProductsPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://web-qa.dev.adalab.es/products'
        self.title = "Catálogo de Productos"
        

    
    def open_products_page(self):
        self.page.goto(self.url)

    def verify_products_category(self, category):
        expect(self.page.get_by_text(category).nth(2)).to_be_visible()

    def verify_products_name(self,product_name):
        expect(self.page.get_by_role("heading", name=product_name)).to_be_visible()

    def verify_products_price(self,price):
        expect(self.page.get_by_text(price)).to_be_visible()

    def verify_products_title(self):
        expect(self.page.locator("h1")).to_contain_text(self.title)

    def verify_products_url(self):
        expect(self.page).to_have_url(self.url)

    def filter_by_palas(self):
        self.page.get_by_role("searchbox", name="Nombre").fill("palas")


from playwright.sync_api import Page


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://web-qa.dev.adalab.es/products'
        self.title = "Catálogo de Productos"

    def navigate(self):
        self.page.goto("https://web-qa.dev.adalab.es/products")

    def filter_by_name(self, name):
        self.page.get_by_role("searchbox", name="Nombre").fill(name)

    def filter_by_category(self, category):
        self.page.get_by_label("Categoría").select_option(category)

    def filter_by_min_price(self, min_price):
        self.page.get_by_role(
            "spinbutton",
            name="Precio mínimo"
        ).fill(min_price)

    def filter_by_max_price(self, max_price):
        self.page.get_by_role("spinbutton",name="Precio máximo").fill(max_price)


from playwright.sync_api import Page
class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://web-qa.dev.adalab.es/products'
        self.title = "Catálogo de Productos"


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://web-qa.dev.adalab.es/products")

    def filter_by_name(self, name):
        self.page.get_by_role("searchbox", name="Nombre").fill(name)

    def get_no_results_message(self):
        return self.page.get_by_text("No se encontraron productos")