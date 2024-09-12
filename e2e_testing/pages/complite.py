class ComplitePage:
    def __init__(self, page):
        self.page = page
        self.complite_header = page.locator("[data-test=\"complete-header\"]")