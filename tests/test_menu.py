from playwright.sync_api import Page, expect

def test_navigation_through_links(page: Page):
    print("When the user enters the 'Vida Verde' page")
    page.goto("https://web-qa.dev.adalab.es/")
    print("When the user clicks on 'Quienes Somos'")
    page.get_by_role("link", name="Quiénes Somos").click()
    print ("And the user clicks on 'Products'")
    page.get_by_role("link", name="Productos").click()
    print ("And the user clicks on 'Contact'")
    page.get_by_role("link", name="Contacto").click()

    print("Then the 'Quienes somos' page is displayed")
    page.get_by_role("link", name="Quiénes Somos").click()
    expect(page.get_by_role("heading", name="Quiénes Somos")).to_be_visible()
    print("Then the 'Productos' page is displayed")
    page.get_by_role("link", name="Productos").click()
    expect(page.get_by_role("heading", name="Productos")).to_be_visible()
    print("Then the 'Contáctanos' page is displayed")
    page.get_by_role("link", name="Contáctanos").click()
    expect(page.get_by_role("heading", name="Contáctanos")).to_be_visible()

     
    
