from playwright.sync_api import Page, expect
from pages.components.menu import Menu
from pages.home_page import HomePage
from pages.about_us_page import AboutusPage
from pages.products_page import ProductsPage
from pages.contacto_page import ContactPage



def test_visit_menu_links(page: Page):
    home_page = HomePage (page)
    menu = Menu(page)
    about_us_page = AboutusPage(page)
    products_page = ProductsPage(page)
    contacto_page = ContactPage(page)
   


    print("When the user enters the 'Vida Verde' page")
    HomePage.open_home_page()

    print("Then they should see the title 'Vida Verde'")
    HomePage.verify_home_page_title()

    print("When the user clicks on 'Quienes Somos'")
    Menu.visit_menu_about_us()

    print("Then they should see the tittle 'Quienes Somos'")
    AboutusPage.verify_about_us_title()

    print("And they should see the URL 'https://web-qa.dev.adalab.es/about'")
    AboutusPage.verify_about_us_url()
    
    print("When the user clicks on 'Productos'")
    Menu.visit_menu_products()

    print("Then they should see the tittle 'Catálogo de Productos'")
    ProductsPage.verify_products_title()

    print("And they should see the URL 'https://web-qa.dev.adalab.es/products'")
    ProductsPage.verify_products_url()

    print("When the user clicks on 'Contacto'")
    Menu.visit_menu_contacto()

    print("Then they should see the tittle 'Contáctanos'")
    ContactPage.verify_contact_title()

    print("And they should see the URL 'https://web-qa.dev.adalab.es/contact'")
    ContactPage.verify_contact_url()







    


   
 




