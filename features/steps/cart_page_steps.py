from selenium.webdriver.common.by import By
from behave import when, then


CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")


@when('Open on cart icon')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')

@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_message(context):
    context.app.cart_page.verify_cart_empty_message()




@then('Add item to cart')
def add_to_cart(context):
    context.app.cart_page.add_to_cart()


@then('navigate to cart')
def open_cart(context):
    context.app.main_page.open_cart()


@then('Verify {expected_item} is shown in cart')
def verify_cart_item(context,expected_item):
    context.app.cart_page.verify_item_cart_page(expected_item)


