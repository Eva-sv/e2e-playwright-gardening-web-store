from playwright.sync_api import Page, expect

url = 'https://web-qa.dev.adalab.es/products'




def test_products_page(page: Page):
    print("When the user enters to the products page")
    page.goto(url)
    print("Then the user should see the product category 'Plants'")
    page.get_by_role("link", name="Productos").click()
    page.get_by_text("Plantas").nth(2).click()
    expect(page.get_by_text("Plantas").nth(2)).to_be_visible()
    print("And the user should see the product name 'Ficus Lyrata'")
    expect(page.get_by_role("heading", name="Ficus Lyrata")).to_be_visible()
    print("And the user should see the product price '35.00€")
    expect(page.get_by_text("35.00 €")).to_be_visible()