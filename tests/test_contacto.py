from playwright.sync_api import Page, expect
from pages.contacto_page import ContactPage

def test_submit_form_empty_required_message(page: Page):
    
    print("Given the user is on the contact page: Contáctanos | Vida Verde")
    page.goto("https://web-qa.dev.adalab.es/contact")
    
    print("When they fill in the required name field")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Díaz")
    
    print("And they fill in the required email field")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    
    print("And they click on submit")
    page.get_by_role("button", name="Enviar Mensaje").click()
    
    print("Then they should see an error message: El mensaje es obligatorio")
    expect(page.get_by_text("El mensaje es obligatorio")).to_be_visible()


from playwright.sync_api import Page, expect

def test_form_with_required_name_field_left_empty(page: Page):
    contact_page = ContactPage(page)
    print("Given the users enters contact page 'Contact| Vida Verde'")
    contact_page.open_contact_page()

    print ("fills required email with 'test@gmail.com'")
    contact_page.fill_contact_email("test@gmail.com")
   
    print ("fills required message with 'test mesage'")
    contact_page.fill_contact_message("test mensaje")

    print ("clicks send")
    contact_page.press_send_contact()

    print ("user should see the error message 'name is mandatory'")
    contact_page.verify_message_form("El nombre es obligatorio")


   
def test_empty_email_field_confirmation(page: Page):
    print("Given the user is on the contact page Contáctanos | Vida Verde  with the email field empty")
    page.goto("https://web-qa.dev.adalab.es/contact")
    print("When the user fills the required fields name and message")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    page.get_by_role("textbox", name="Mensaje *").fill("Test")
    page.get_by_role("button", name="Enviar Mensaje").click()
    print("Then the error message is displayed: El email es obligatorio ")
    expect(page.get_by_text("El email es obligatorio")).to_be_visible()



def test_submit_form_with_invalid_emails(page: Page):
    print("Given the user is on the contact page Contáctanos | Vida Verde")
    page.goto("https://web-qa.dev.adalab.es/contact")
    print("When the user fills the required fields name whith 'Marta Diaz'")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    print("and the user fills the required fields whith an invalid email")
    page.get_by_role("textbox", name="Email *").fill("email")
    print("and the user fills the required fields test messaje with 'Test mensaje'")
    page.get_by_role("textbox", name="Mensaje *").fill("test mensaje")
    page.get_by_role("button", name="Enviar Mensaje").click()
    print("Then the error message is displayed: El email no es válido")
    expect(page.get_by_text("El formato del email no es vá")).to_be_visible()

def test_submit_forms_with_valid_required_fields(page: Page):
    print("Given the user is on the contact page Contáctanos | Vida Verde")
    page.goto("https://web-qa.dev.adalab.es/contact")
    print("When the user fills Fill in the name with 'Marta Diaz'")
    page.get_by_role("textbox", name="Nombre *").fill("marta Diaz")
    print("And fill in the email with 'test_automation@test.com'")
    page.get_by_role("textbox", name="Email *").fill("test_automation@test.com")
    print("And fill in the message with 'test mensaje'")
    page.get_by_role("textbox", name="Mensaje *").fill("test mensaje")
    page.get_by_role("button", name="Enviar Mensaje").click()
    expect(page.get_by_role("heading", name="¡Mensaje enviado con éxito!")).to_be_visible()
    
    
   