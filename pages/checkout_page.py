from playwright.sync_api import Page, expect

class CheckoutPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://web-qa.dev.adalab.es/checkout'
        self.title = "Finalizar Compra"

    def verify_order_summary(self):
        expect(self.page.get_by_role("heading", name="Resumen del Pedido")).to_be_visible()
        expect(self.page.get_by_text("Juego de Palas15.99 €")).to_be_visible()
        expect(self.page.get_by_text("Subtotal (1)15.99 €")).to_be_visible()
        expect(self.page.get_by_text("IVA (21%)3.36 €")).to_be_visible()
        expect(self.page.get_by_text("Envío5.00 €")).to_be_visible()
        expect(self.page.get_by_text("Total24.35 €")).to_be_visible()

    def fill_valid_name_field(self):
        self.page.get_by_role("textbox", name="Nombre Completo *").fill("Maria Diaz")

    def fill_valid_email_field(self):
         self.page.get_by_role("textbox", name="Email *").fill("test@gmail.com")

    def fill_valid_adress(self):
         self.page.get_by_role("textbox", name="Dirección *").fill("CAlle Aragon, 25, Madrid")

    def add_credit_card(self, card_number):
         self.page.get_by_role("textbox", name="Número de Tarjeta de Crédito *").fill(card_number)

    def click_complete_purchase(self):
        self.page.get_by_role("button", name="Completar Compra").click()

    def verify_message_purchase_completed_succesfully(self):
        expect(self.page.get_by_role("heading", name="¡Compra Realizada con Éxito!")).to_be_visible()

    def click_back_store(self):
        self.page.get_by_role("link", name="Volver a la Tienda").click()

    def verify_see_products_page(self):
        expect(self.page.get_by_role("heading", name="Catálogo de Productos")).to_be_visible()

    #def fill_invalid_card_number(self):
        #self.page.get_by_role("textbox", name="Número de Tarjeta de Crédito *").click()
        #self.page.get_by_role("textbox", name="Número de Tarjeta de Crédito *").fill("1111424242424242")
    
    def click_complete_purchase(self):
        self.page.get_by_role("button", name="Completar Compra").click()

    def verify_message_invalid_card(self):
        expect(self.page.get_by_text("Tarjeta de crédito no válida.")).to_be_visible()

    def verify_remain_checkout_page_and_url_checkout(self):
        expect(self.page.get_by_role("heading", name="Finalizar Compra")).to_be_visible()



    

        

 

        