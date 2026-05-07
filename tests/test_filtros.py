
from playwright.sync_api import Page, expect

def test_filter_by_valid_name_price_and_category(page: Page):
    print("Given the user opens the products page 'Nuestros Productos | Vida Verde'")
    page.goto("https://web-qa.dev.adalab.es/products")
    print("When the user filters by name 'Regadera'")
    page.get_by_role("searchbox", name="Nombre").fill("regadera")
    print("And filters by category 'Herramientas'")
    page.get_by_label("CategoríaTodas las categorí").select_option("Herramientas")
    print("And filters by minimum price '20'")
    page.get_by_role("spinbutton", name="Precio mínimo").fill("20")
    print("And filters by maximum price '25'")
    page.get_by_role("spinbutton", name="Precio máximo").fill("25")
    expect(page.get_by_text("No se encontraron productos")).to_be_visible()

   