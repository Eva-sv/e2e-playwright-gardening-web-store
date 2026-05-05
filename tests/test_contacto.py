from playwright.sync_api import Page, expect

def test_submit_form_with_required_message_field_left_empty(page: Page):
    print('Given the user enters the contact page "Contáctanos | Vida Verde"')
    page.goto("https://web-qa.dev.adalab.es/contact")
    print("when they fill in the required name field")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    print("And they fill in the required email field")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    print("And they click Submit")
    page.get_by_role("button", name="Enviar Mensaje").click()
    print('Then they should see an error message: "Message is required"')
    expect(page.get_by_text("El mensaje es obligatorio")).to_be_visible()


from playwright.sync_api import Page, expect

def test_Submit_form_with_required_name_field_empty(page: Page):
    print('Given the user enters the contact page "Contáctanos | Vida Verde"')
    page.goto("https://web-qa.dev.adalab.es/contact")
    print("When they fill in the required email field with 'test@gmail.com'")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")
    print("and fill in the required message field with 'test message'")
    page.get_by_role("textbox", name="Mensaje *").fill("test mensaje")
    print("And they click Submit")
    page.get_by_role("button", name="Enviar Mensaje").click()
    print('Then they should see an error message "El nombre es obligatorio"')
    expect(page.get_by_text("El nombre es obligatorio")).to_be_visible()
   
def test_empty_email_field_confirmation(page: Page):
    print("Given the user is on the contact page Contáctanos | Vida Verde  with the email field empty")
    page.goto("https://web-qa.dev.adalab.es/contact")
    print("When the user fills the required fields name and message")
    page.get_by_role("textbox", name="Nombre *").fill("Marta Diaz")
    page.get_by_role("textbox", name="Mensaje *").fill("Test")
    page.get_by_role("button", name="Enviar Mensaje").click()
    print("Then then the error message is displayed: El email es obligatorio ")
    expect(page.get_by_text("El email es obligatorio")).to_be_visible()
    
   