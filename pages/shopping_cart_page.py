from playwright.sync_api import Page, expect

class ShoppingcartPage:
    def __init__(self, page: Page):
         self.page = page
         
    
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
