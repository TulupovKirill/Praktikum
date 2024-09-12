from playwright.sync_api import expect

from pages.login import LoginPage
from pages.product import ProductPage
from pages.shopping_cart import ShopingCartPage
from pages.checkout import CheckoutPage
from pages.overview import OverviewPage
from pages.complite import ComplitePage

def test_enters_correct_data_to_place_a_order(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    cart_page = ShopingCartPage(page)
    checkout_page = CheckoutPage(page)
    overview_page = OverviewPage(page)
    complite_page = ComplitePage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    login_page.login_click()
    product_page.button_add_to_cart_sauce_labs_backpack.click()
    product_page.button_shopping_cart_link.click()
    cart_page.button_checkout.click()
    checkout_page.enters_data("name", "lastname", "myemail@mail.ru")
    checkout_page.button_continue.click()
    overview_page.button_finish.click()
    expect(complite_page.complite_header).to_have_text("Thank you for your order!")