from playwright.sync_api import Page, expect
from menu_page import MenuPage

url = 'https://web-qa.dev.adalab.es'

def test_navigation_through_about_link(page: Page):
    print("When the user enters the 'Vida Verde' page")
    #page.goto(url)
    MenuPage.open_menu_page()
    print("When the user clicks on 'Quienes Somos'")
    page.get_by_role("link", name="Quiénes Somos").click()
    expect(page.get_by_role("heading", name="Quiénes Somos")).to_be_visible()
    expect(page).to_have_url(f'{url}/about')

def test_navigation_through_products_links(page: Page):
    print("When the user enters the 'Vida Verde' page")
    page.goto(url)
    print("When the user clicks on 'Products'")
    page.get_by_role("link", name="Productos", exact=True).click()
    expect(page.get_by_role("heading", name="Productos")).to_be_visible()
    expect(page).to_have_url(f'{url}/products')

def test_navigation_through_contact_links(page: Page):
    print("When the user enters the 'Vida Verde' page")
    page.goto(url)
    print("When the user clicks on 'Contact Us'")
    page.get_by_role("link", name="Contacto").click()
    expect(page.get_by_role("heading", name="Contacto")).to_be_visible()
    expect(page).to_have_url(f'{url}/contact')

