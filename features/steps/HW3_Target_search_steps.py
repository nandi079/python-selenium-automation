from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Target main page open')
def target_main_page(context):
    context.driver.get('https://www.target.com')

@when('Click on Cart icon')
def Cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@then('find Your cart is empty')
def find_cart_is_empty(context):
    context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles__StyledHeading']")
    sleep(4)

