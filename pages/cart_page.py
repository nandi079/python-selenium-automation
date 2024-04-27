from selenium.webdriver.common.by import By

from pages.base_page import Page
from time import sleep

class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    ADD_CART_PRODUCT = (By.CSS_SELECTOR, "[id='addToCartButtonOrTextIdFor12954582']")
    ADD_NAV_CART_PRODUCT = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")

    ITEM_IN_CART = (By.CSS_SELECTOR, "[data-test='cartItem-linked-title']")

    def verify_cart_empty_message(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)



    def add_to_cart(self):
        self.click(*self.ADD_CART_PRODUCT)
        sleep(5)
        self.click(*self.ADD_NAV_CART_PRODUCT)


    def navigate_to_cart(self):
        context.app.main_page.open_cart_page()


    def verify_item_cart_page(self,expected_item):
        self.verify_partial_text(expected_item, *self.ITEM_IN_CART)







#def verify_cart_empty_message(self):
        #actual_text = self.find_element(*self.CART_EMPTY_MSG).text
        #expected_text = 'Your cart is empty'
        #assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'
 #       self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)
