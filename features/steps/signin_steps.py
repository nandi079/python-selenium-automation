from selenium.webdriver.common.by import By
from behave import then


SIGNIN_BUTTON = (By.XPATH, "[aria-label='Account, sign in']")
NAV_BUTTON = (By.XPATH, "a[data-test='accountNav-signIn']")

#  Then Click on Target Signin button
#    Then Click on Signin button on right side navigation
#    Then Verify Signin form opened


@then('Click on Target Signin button')
def target_signin_button(context):
    context.app.signin_page.click_target_signin_button()


@then('Click on Signin button on right side navigation')
def click_nav_signin_button(context):
    context.app.signin_page.click_nav_signin_button()

@then('Verify Signin page opened')
def verify_signin_page(context):
    context.app.signin_page.verify_signin_page()
