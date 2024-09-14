class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("[data-test=\"username\"]")
        self.password = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")
        self.title = page.locator("[data-test=\"title\"]")
        self.error = page.locator("[data-test=\"error\"]")

    def navigate(self) -> None:
        self.page.goto("https://www.saucedemo.com")

    def login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
    
    def login_click(self) -> None:
        self.login_button.click()