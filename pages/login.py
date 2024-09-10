class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator('[data-test=\\"username\\"]')
        self.password = page.locator('[data-test=\\"password\\"]')
        self.login_button = page.locator('[data-test=\\"login-button\\"]')
        self.title = page.locator('[data-test=\\"title\\"]')

    def navigate(self):
        self.page.goto("<https://www.saucedemo.com/>")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()