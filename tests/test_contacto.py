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

    print("Given user visit homepage")
    page.goto("https://web-qa.dev.adalab.es")
    
