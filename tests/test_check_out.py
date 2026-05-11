from playwright.sync_api import Page, expect
from check_out_page import CheckoutPage
from products_page import ProductsPage
from shopping_cart_page import ShoppingcartPage


def test_checkout_with_valid_payment_details(page: Page):
    products_page = ProductsPage(page)
    check_out_page = CheckoutPage(page)
    shopping_cart_page = ShoppingcartPage(page)


    
    # Logica del ProductsPAge
    print("When the user enters to the products page")
    ProductsPage.open_products_page()

    print("When they filter by name 'palas'")
    page.get_by_role("searchbox", name="Nombre").fill("palas")
    print("And add the product to the cart")
    page.get_by_role("button", name="Añadir Juego de Palas al").click()
    print("And visit the cart page")
    page.get_by_role("link", name="Carrito de compra").click()
    
    # Logica del CartsPage
    print("And click on 'Proceed to checkout'")
    page.get_by_role("link", name="Proceder al Pago").click()
    
    print("Then they should see the order summary with:'product:juego de palas','price: 15.99', 'subtotal:15.99','iva: 3.36', 'shipping: 5', 'total: 24'")
    #ShoppingCartPage.verify_order_summary()

    print("When they fill in the valid name field 'Maria Diaz'")
    CheckoutPage.verify_valid_name_field()

    print("And fill in the valid email field")
    CheckoutPage.verify_valid_email_field()

    print("And fill in the valid adress 'Calle Aragón, 25, Madrid'")
    CheckoutPage.verify_valid_adress()

    print("And add a valid card number '4242 4242 4242 4242'")
    CheckoutPage.verify_valid_card_number()

    print("And click on 'Complete purchase'")
    CheckoutPage.verify_click_complete_purchase()

    print("Then they should see the message 'Purchase completed successfully")
    CheckoutPage.verify_message_purchase_completed_succesfully()

    print("And they should see the completed order page with: 'Resumen del pedido")
    CheckoutPage.verify_order_summary()

    print("When they click on 'Back to store'")
    CheckoutPage.verify_click_back_store()

    print("Then they should see the products page: https://web_qa.dev.adalab.es/products")
    CheckoutPage.verify_see_products_page()

    
def test_checkout_with_invalid_card_details(page: Page):
    print("When the user enters to the products page")
    ProductsPage.open_products_page()

    print("When they filter by name 'palas'")
    page.get_by_role("searchbox", name="Nombre").fill("palas")

    print("And add the product to the cart")
    page.get_by_role("button", name="Añadir Juego de Palas al").click()

    print("And visit the cart page")
    page.get_by_role("link", name="Carrito de compra").click()

    print("And click on 'Proceed to checkout'")
    page.get_by_role("link", name="Proceder al Pago").click()

    print("When they fill in the valid name field 'Maria Diaz'")
    CheckoutPage.verify_valid_name_field()

    print("And fill in the valid email field")
    CheckoutPage.verify_valid_email_field()

    print("And fill in the valid adress 'Calle Aragón, 25, Madrid'")
    CheckoutPage.verify_valid_adress()

    print("And add an invalid card number '1111 4242 4242 4242'")
    CheckoutPage.verify_invalid_card_number()

    print("And click on 'Complete purchase'")
    CheckoutPage.verify_click_complete_purchase()

    print("Then they should see a message with 'Tarjeta de crédito no válida'")
    CheckoutPage.verify_invalid_card_number()


def test_checkout_without_card_details(page: Page):

    print("When the user enters to the products page")
    ProductsPage.open_products_page()

    print("When they filter by name 'palas'")
    page.get_by_role("searchbox", name="Nombre").fill("palas")

    print("And add the product to the cart")
    page.get_by_role("button", name="Añadir Juego de Palas al").click()

    print("And visit the cart page")
    page.get_by_role("link", name="Carrito de compra").click()

    print("And click on 'Proceed to checkout'")
    page.get_by_role("link", name="Proceder al Pago").click()

    print("When they fill in the valid name field 'Maria Diaz'")
    CheckoutPage.verify_valid_name_field()

    print("And fill in the valid email field")
    CheckoutPage.verify_valid_email_field()

    print("And fill in the valid adress 'Calle Aragón, 25, Madrid'")
    CheckoutPage.verify_valid_adress()

    print("And click on 'Complete purchase'")
    CheckoutPage.verify_click_complete_purchase()
    
    print("Then the user should remain on the checkout page and the page URL should be 'https://web-qa.dev.adalab.es/checkout'")
    CheckoutPage.verify_remain_checkout_page_and_url_checkout()

    