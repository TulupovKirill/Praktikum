class ShopingCartPage:
    def __init__(self, page):
        self.page = page
        self.inventoty_item = page.locator("[data-test=\"inventory-item\"]")
        self.button_checkout = page.locator("[data-test=\"checkout\"]")
        
