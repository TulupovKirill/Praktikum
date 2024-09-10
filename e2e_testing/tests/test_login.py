from playwright.sync_api import expect

from pages.login import LoginPage

def test_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")