from selenium.webdriver.common.by import By
from behave import when, then


CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
PRODUCT_SELECTOR = (By.CSS_SELECTOR, "input[value='bottle']")

@when('Open on cart icon')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_message(context):
    context.app.cart_page.verify_cart_empty_message()


@then('Verify product has shown in chart')
def verify_cart_item(context):
    context.app.cart_page.verify_cart_page()