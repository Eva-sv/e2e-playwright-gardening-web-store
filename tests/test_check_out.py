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
    products_page.open_products_page()

    print("When they filter by name 'palas'")
    products_page.filter_by_palas()

    print("And add the product to the cart")
    products_page.click_product_to_the_cart()

    print("And visit the cart page")
    products_page.click_cart_page()
    
    # Logica del CartsPage
    print("And click on 'Proceed to checkout'")
    shopping_cart_page.click_proceed_to_check_out()
    
    print("Then they should see the order summary with:'product:juego de palas','price: 15.99', 'subtotal:15.99','iva: 3.36', 'shipping: 5', 'total: 24'")
    shopping_cart_page.verify_order_summary()

    print("When they fill in the valid name field 'Maria Diaz'")
    check_out_page.fill_valid_name_field()

    print("And fill in the valid email field")
    check_out_page.fill_valid_email_field()

    print("And fill in the valid adress 'Calle Aragón, 25, Madrid'")
    check_out_page.fill_valid_adress()

    print("And add a valid card number '4242 4242 4242 4242'")
    check_out_page.fill_valid_card_number()

    print("And click on 'Complete purchase'")
    check_out_page.click_complete_purchase()

    print("Then they should see the message 'Purchase completed successfully")
    check_out_page.verify_message_purchase_completed_succesfully()

    print("And they should see the completed order page with: 'Resumen del pedido")
    check_out_page.verify_order_summary()

    print("When they click on 'Back to store'")
    check_out_page.click_back_store()

    print("Then they should see the products page: https://web_qa.dev.adalab.es/products")
    check_out_page.verify_see_products_page()

    
def test_checkout_with_invalid_card_details(page: Page):
    
    print("When the user enters to the products page")
    prod.open_products_page()

    print("When they filter by name 'palas'")
    pro.filter_by_palas()

    print("And add the product to the cart")
    ProductsPage.click_product_to_the_cart()

    print("And visit the cart page")
    ProductsPage.click_cart_page()

    print("And click on 'Proceed to checkout'")
    ShoppingcartPage.click_proceed_to_check_out()

    print("When they fill in the valid name field 'Maria Diaz'")
    CheckoutPage.fill_valid_name_field()

    print("And fill in the valid email field")
    CheckoutPage.fill_valid_email_field()

    print("And fill in the valid adress 'Calle Aragón, 25, Madrid'")
    CheckoutPage.fill_valid_adress()

    print("And add an invalid card number '1111 4242 4242 4242'")
    CheckoutPage.fill_invalid_card_number()

    print("And click on 'Complete purchase'")
    CheckoutPage.click_complete_purchase()

    print("Then they should see a message with 'Tarjeta de crédito no válida'")
    CheckoutPage.fill_invalid_card_number()


def test_checkout_without_card_details(page: Page):

    print("When the user enters to the products page")
    ProductsPage.open_products_page()

    print("When they filter by name 'palas'")
    ProductsPage.filter_by_palas()

    print("And add the product to the cart")
    ProductsPage.click_product_to_the_cart()

    print("And visit the cart page")
    ProductsPage.click_cart_page()

    print("And click on 'Proceed to checkout'")
    ShoppingcartPage.click_proceed_to_check_out()

    print("When they fill in the valid name field 'Maria Diaz'")
    CheckoutPage.fill_valid_name_field()

    print("And fill in the valid email field")
    CheckoutPage.fill_valid_email_field()

    print("And fill in the valid adress 'Calle Aragón, 25, Madrid'")
    CheckoutPage.fill_valid_adress()

    print("And click on 'Complete purchase'")
    CheckoutPage.click_complete_purchase()
    
    print("Then the user should remain on the checkout page and the page URL should be 'https://web-qa.dev.adalab.es/checkout'")
    CheckoutPage.verify_remain_checkout_page_and_url_checkout()

    