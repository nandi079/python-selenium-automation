from pages.base_page import Page


class MainPage(Page):

    def open_main(self):
        self.driver.get('https://www.target.com/')

    def open_cart(self):
        self.driver.get('https://www.target.com/cart')