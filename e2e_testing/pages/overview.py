class OverviewPage:
    def __init__(self, page):
        self.page = page
        self.button_finish = page.locator("[data-test=\"finish\"]")