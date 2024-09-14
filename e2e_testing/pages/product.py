class ProductPage:
    def __init__(self, page):
        self.page = page
        self.button_add_to_cart_sauce_labs_backpack = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.button_add_to_cart_sauce_labs_bike_light = page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]")
        self.button_shopping_cart_link = page.locator("[data-test=\"shopping-cart-link\"]")
    