from playwright.sync_api import Page, expect

class ShoppingcartPage:
    def __init__(self, page: Page):
         self.page = page
         self.url = 'https://web-qa.dev.adalab.es/cart'
         
    
#EVA

    def click_proceed_to_check_out(self):
        self.page.get_by_role("link", name="Proceder al Pago").click()

    def verify_order_summary(self):
        expect(self.page.get_by_role("heading", name="Resumen del Pedido")).to_be_visible()
        expect(self.page.get_by_text("Juego de Palas15.99 €")).to_be_visible()
        expect(self.page.get_by_text("Subtotal (1)15.99 €")).to_be_visible()
        expect(self.page.get_by_text("IVA (21%)3.36 €")).to_be_visible()
        expect(self.page.get_by_text("Envío5.00 €")).to_be_visible()
        expect(self.page.get_by_text("Total24.35 €")).to_be_visible()

#Yohana
    def open_shopping_cart_page(self):
        self.page.goto(self.url)
    
    def verify_shopping_cart_by_product_name(self, product_name):
        expect(self.page.get_by_role("heading", name=product_name)).to_be_visible()

    def verify_shopping_cart_by_product_category(self, category):
        expect(self.page.get_by_text(category)).to_be_visible()
    
    def verify_shopping_cart_by_product_price(self, price):
        expect(self.page.get_by_text(price)).to_be_visible()
    
    def verify_shopping_cart_summary(self, subtotal, tax, shipping, total):
        expect(self.page.get_by_role("heading", name="Resumen del Pedido")).to_be_visible()
        expect(self.page.get_by_text("32.50 €")).to_be_visible()
        expect(self.page.get_by_text("6.83 €")).to_be_visible()
        expect(self.page.get_by_text("5.00 €")).to_be_visible()
        expect(self.page.get_by_text("44.33 €")).to_be_visible()

    def click_empty_cart_button(self):
       self.page.get_by_role("button", name="Vaciar Carrito").click()
    
    def verify_empty_cart_message(self):
        expect(self.page.get_by_text("Tu carrito está vacío")).to_be_visible()
