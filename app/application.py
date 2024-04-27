from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.signin_page import SignInPage




class Application:

    def __init__(self, driver):
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.signin_page = SignInPage(driver)








































#app = Application(driver)  ## no need to this element, added in environment.py..
#app.main_page              ##..context.app = Application(context.driver)
#app.header
#app.search_result_page
