class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.field_firstName = page.locator("[data-test=\"firstName\"]")
        self.field_lastName = page.locator("[data-test=\"lastName\"]")
        self.field_email = page.locator("[data-test=\"postalCode\"]")
        self.button_continue = page.locator("[data-test=\"continue\"]")
    
    def enters_data(self, firstName: str, lastName: str, email: str):
        self.field_firstName.fill(firstName)
        self.field_lastName.fill(lastName)
        self.field_email.fill(email)
