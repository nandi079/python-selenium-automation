from selenium.webdriver.common.by import By

from pages.base_page import Page
from time import sleep

class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    ADD_CART_PRODUCT = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")


    def verify_cart_empty_message(self):
        #actual_text = self.find_element(*self.CART_EMPTY_MSG).text
        #expected_text = 'Your cart is empty'
        #assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)



    def verify_cart_page(self):
        self.verify_text( 'Verifying product page', *self.ADD_CART_PRODUCT)







