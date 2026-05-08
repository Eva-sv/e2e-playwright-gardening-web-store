from playwright.sync_api import Page, expect

url = 'https://web-qa.dev.adalab.es/products'

def test_checkout_with_valid_payment_details(page: Page):
    print("When the user enters to the products page")
    page.goto(url)
    print("When they filter by name 'palas'")
    page.get_by_role("searchbox", name="Nombre").fill("palas")
    print("And add the product to the cart")
    page.get_by_role("button", name="Añadir Juego de Palas al").click()
    print("And visit the cart page")
    page.get_by_role("link", name="Carrito de compra").click()
    
    print("And click on 'Proceed to checkout'")
    page.get_by_role("link", name="Proceder al Pago").click()
    print("Then they should see the order summary with:'product:juego de palas','price: 15.99', 'subtotal:15.99','iva: 3.36', 'shipping: 5', 'total: 24'")
    expect(page.get_by_text("Juego de Palas")).to_be_visible()
     
    # Locate the row containing "Juego de Palas"
    product_row = page.locator("li.flex", has_text="Juego de Palas")

    # Validate product name
    expect(product_row.locator("data")).to_have_text("15.99 €")

       # Locate the row containing "Subtotal (1)"
    subtotal_row = page.locator("div.flex", has_text="Subtotal (1)")

    # Locate the contiguous <data> element inside that row
    subtotal_data = subtotal_row.locator("data")
    expect(subtotal_data).to_have_text("15.99 €")


    expect(page.get_by_text("15.99")).to_be_visible()
    expect(page.get_by_text("3.36")).to_be_visible()
    expect(page.get_by_text("5")).to_be_visible()
    expect(page.get_by_text("24")).to_be_visible()
    expect(page.get_by_role("complementary", name="Resumen del Pedido")).to_be_visible()

    print("When they fill in the valid name field 'Maria Diaz'")
    page.get_by_role("textbox", name="Nombre Completo *").fill("Maria Diaz")
    print("And fill in the valid email field")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    print("And fill in the valid adress 'Calle Aragón, 25, Madrid'")
    page.get_by_role("textbox", name="Dirección *").fill("CAlle Aragon, 25, Madrid")
    print("And add a valid card number '4242 4242 4242 4242'")
    page.get_by_role("textbox", name="Número de Tarjeta de Crédito *").fill("4242424242424242")
    print("And click on 'Complete purchase'")
    page.get_by_role("button", name="Completar Compra").click()
    print("Then they should see the message 'Purchase completed successfully")
    expect(page.get_by_role("heading", name="¡Compra Realizada con Éxito!")).to_be_visible()
    print("And they should see the completed order page with: 'Resumen del pedido")
    expect(page.get_by_role("region", name="Resumen del Pedido")).to_be_visible()
    expect(page.get_by_text("Juego de Palas")).to_be_visible()
    expect(page.get_by_text("15.99")).to_be_visible()
    expect(page.get_by_text("15.99")).to_be_visible()
    expect(page.get_by_text("3.36")).to_be_visible()
    expect(page.get_by_text("5")).to_be_visible()
    expect(page.get_by_text("24")).to_be_visible()
    print("When they click on 'Back to store'")
    page.get_by_role("link", name="Volver a la Tienda").click()
    print("Then they should see the products page: https://web_qa.dev.adalab.es/products")
    expect(page.get_by_role("heading", name="Catálogo de Productos")).to_be_visible()
 

def test_checkout_with_invalid_card_details(page: Page):
    print("When the user enter")
    page.goto(url)
    page.get_by_role("searchbox", name="Nombre").click()
    page.get_by_role("searchbox", name="Nombre").click()
    page.get_by_role("searchbox", name="Nombre").fill("palas")
    page.get_by_role("button", name="Añadir Juego de Palas al").click()
    page.get_by_role("link", name="Carrito de compra").click()
    page.get_by_role("link", name="Proceder al Pago").click()
    page.get_by_role("textbox", name="Nombre Completo *").click()
    page.get_by_role("textbox", name="Nombre Completo *").press("CapsLock")
    page.get_by_role("textbox", name="Nombre Completo *").fill("M")
    page.get_by_role("textbox", name="Nombre Completo *").press("CapsLock")
    page.get_by_role("textbox", name="Nombre Completo *").fill("MAria ")
    page.get_by_role("textbox", name="Nombre Completo *").press("CapsLock")
    page.get_by_role("textbox", name="Nombre Completo *").fill("MAria Diaz")
    page.get_by_role("textbox", name="Email *").click()
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    page.get_by_role("textbox", name="Dirección *").click()
    page.get_by_role("textbox", name="Dirección *").press("CapsLock")
    page.get_by_role("textbox", name="Dirección *").fill("C")
    page.get_by_role("textbox", name="Dirección *").press("CapsLock")
    page.get_by_role("textbox", name="Dirección *").fill("Calle ")
    page.get_by_role("textbox", name="Dirección *").press("CapsLock")
    page.get_by_role("textbox", name="Dirección *").fill("Calle A")
    page.get_by_role("textbox", name="Dirección *").press("CapsLock")
    page.get_by_role("textbox", name="Dirección *").fill("Calle Aragón, 25, ")
    page.get_by_role("textbox", name="Dirección *").press("CapsLock")
    page.get_by_role("textbox", name="Dirección *").fill("Calle Aragón, 25, M")
    page.get_by_role("textbox", name="Dirección *").press("CapsLock")
    page.get_by_role("textbox", name="Dirección *").fill("Calle Aragón, 25, Madrid")
    page.get_by_role("textbox", name="Número de Tarjeta de Crédito *").click()
    page.get_by_role("textbox", name="Número de Tarjeta de Crédito *").fill("1111424242424242")
    page.get_by_role("button", name="Completar Compra").click()
    page.get_by_role("button", name="Completar Compra").click()
    page.get_by_role("button", name="Completar Compra").click()
    page.get_by_role("button", name="Completar Compra").click()
    page.get_by_role("button", name="Completar Compra").click()
    expect(page.get_by_text("El número de tarjeta debe")).to_be_visible()

    
    

