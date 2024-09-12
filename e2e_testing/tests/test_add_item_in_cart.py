from playwright.sync_api import expect

from pages.login import LoginPage
from pages.product import ProductPage
from pages.shopping_cart import ShopingCartPage

def test_add_item_in_card(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    cart_page = ShopingCartPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    login_page.login_click()
    product_page.button_add_to_cart_sauce_labs_backpack.click()
    product_page.button_shopping_cart_link.click()
    expect(cart_page.inventoty_item).to_have_count(1)
    