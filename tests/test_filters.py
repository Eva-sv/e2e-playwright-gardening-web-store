from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage


def test_filter_by_valid_name_price_and_category(page: Page):
    products_page = ProductsPage(page)

    print("Given the user opens the product page")
    products_page.open_products_page()

    print("When filtering by name 'Regadera'")
    products_page.filter_by_name("Regadera")

    print("And filtering by category 'Herramientas'")
    products_page.filter_by_category("Herramientas")

    print("And filtering by minimum price '20'")
    products_page.filter_by_min_price("20")

    print("And filtering by maximum price '25'")
    products_page.filter_by_max_price("25")

    print("Then should see 'Regadera Metálica'")
    products_page.verify_filtered_product("Regadera Metálica")



def test_filter_without_results(page: Page):
    products_page = ProductsPage(page)

    print("Given the user opens the product page")
    products_page.open_products_page()

    print("When filtering by name with no results 'manzana'")
    products_page.filter_by_name("manzana")

    print("Then the user should see the message 'No se encontraron productos'")
    products_page.get_no_results_message("No se encontraron productos")


