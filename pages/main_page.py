from pages.base_page import Page


class MainPage(Page):

    def open_main(self):
        self.driver.get('https://www.target.com/')

    def open_cart(self):
        self.driver.get('https://www.target.com/cart')

    def open_sign_in(self):
        self.driver.get('https://www.target.com/c/target-app/')

    def open_target_sign_in_page(self):
        self.driver.get('https://www.target.com/login')