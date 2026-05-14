from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage


def test_filter_by_valid_name_price_and_category(page: Page):
    products_page = ProductsPage(page)

    print("Given la usuaria abre la página de productos")
    products_page.open_products_page()

    print("When filtra por nombre 'Regadera'")
    products_page.filter_by_name("Regadera")

    print("And filtra por categoría 'Herramientas'")
    products_page.filter_by_category("Herramientas")

    print("And filtra por precio mínimo '20'")
    products_page.filter_by_min_price("20")

    print("And filtra por precio máximo '25'")
    products_page.filter_by_max_price("25")

    print("Then debe ver Regadera Metálica")
    products_page.verify_filtered_product("Regadera Metálica")



def test_filter_without_results(page: Page):
    products_page = ProductsPage(page)

    print("Given la usuaria visita la página de productos")
    products_page.navigate()

    print("When filtra por nombre sin resultados")
    products_page.filter_by_name("manzana")

    print("Then debe ver mensaje de no productos")
    expect(products_page.get_no_results_message()).to_be_visible()


