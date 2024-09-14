from playwright.sync_api import expect

from pages.login import LoginPage

def test_void_auth_field(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("", "")
    login_page.login_click()
    expect(login_page.error).to_have_text("Epic sadface: Username is required")