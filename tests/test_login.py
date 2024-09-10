from playwright.sync_api import expect

from pages.login import LoginPage
from pages.products_po import ProductsPage

def test_login(page):
    login_page = LoginPage(page)
    productsPage = ProductsPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    expect(productsPage.title_exist()).to_be_visible()