from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage
from pages.shopping_cart_page import ShoppingcartPage

def test_add_products_to_cart_view_summary_and_empty_cart(page: Page):
    products_page = ProductsPage(page) 
    print("Given user visit the page 'Productos | Vida Verde'")
    products_page.open_products_page()

    print("when the user filters by name 'Sansevieria'")
    products_page.filter_by_name("Sansevieria")    

    print("And the user clicks on the add to cart button")
    products_page.adds_product_to_cart("Sansevieria")

    print("And the user clean the filters and see all the products") 
    products_page.clear_filters()
    

    print("And the user adds the Maceta de Barro Grande to the cart")
    products_page.filter_by_name("maceta de barro")
    

    print("And the user clicks on the add to cart button")
    products_page.adds_product_to_cart("Maceta de Barro Grande")

    print("And the user clicks on the shopping cart link")
    products_page.click_cart_page()

    print("And the user sees the Shopping Cart page")
    shopping_cart_page = ShoppingcartPage(page)
    shopping_cart_page.open_shopping_cart_page()    

    print("Then the user should see the shopping cart summary with the products added")
    shopping_cart_page.verify_shopping_cart_by_product_name("Sansevieria")
    shopping_cart_page.verify_shopping_cart_by_product_category("Plantas")
    shopping_cart_page.verify_shopping_cart_by_product_price("22.00 €")

    shopping_cart_page.verify_shopping_cart_by_product_name("Maceta de Barro Grande")
    shopping_cart_page.verify_shopping_cart_by_product_category("Macetas")
    shopping_cart_page.verify_shopping_cart_by_product_price("10.50 €")
    shopping_cart_page.verify_shopping_cart_summary("32.50 €", "6.83 €", "5.00 €", "44.33 €")
    
    print("When the user clicks on the empty cart button")
    shopping_cart_page.click_empty_cart_button()
    
    print("Then the user should see the message 'Tu carrito está vacío'")
    shopping_cart_page.verify_empty_cart_message()
    
  

from playwright.sync_api import Page, expect

def test_remove_products_from_cart_and_view_summary(page: Page):

    print("Given user visit the page 'Productos | Vida Verde'")
    page.goto("https://web-qa.dev.adalab.es/products")
    print("When the user adds the Ficus to the cart")
    page.get_by_role("searchbox", name="Nombre").fill("ficus")
    print("And the user clicks on the add to cart button")
    products_page = ProductsPage(page)
    products_page.adds_product_to_cart("Ficus Lyrata")
    page.get_by_role("button", name="Añadir Ficus Lyrata al carrito").click()
    print("And the user clean the filters and see all the products")    
    page.get_by_role("button", name="Quitar filtros y ver todos").click()
    print("And the user adds the Tijeras de Podar to the cart")
    page.get_by_role("searchbox", name="Nombre").fill("tijeras")
    page.get_by_role("button", name="Añadir Tijeras de Podar al carrito").click()
    print("And the user clicks on the shopping cart link")
    page.get_by_role("link", name="Carrito de compra").click()
    print("And the user removes the Ficus from the cart")
    page.get_by_role("button", name="Eliminar Ficus Lyrata del carrito").click()
    expect(page.get_by_role("heading", name="Ficus Lyrata")).not_to_be_visible()
    expect(page.get_by_role("heading", name="Resumen del Pedido")).to_be_visible()
    expect(page.get_by_label("Resumen del Pedido").get_by_text("18.50 €")).to_be_visible()
    expect(page.get_by_text("3.88 €")).to_be_visible()
    expect(page.get_by_text("5.00 €")).to_be_visible()
    expect(page.get_by_text("27.38 €")).to_be_visible()


