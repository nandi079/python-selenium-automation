from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Browser to Target page')
def Target_page(context):
    context.driver.get('https://www.target.com')
    sleep(5)

@when('Select Sign-In')
def Select_Sign_In(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Account, sign in']").click()
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()
    sleep(3)

@then('Create an account')
def Create_an_account(context):
    context.driver.find_element(By.CSS_SELECTOR, "form[method='post']")
    context.driver.find_element(By.CSS_SELECTOR, "input[name='username'][inputmode='email']")
    context.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    sleep(3)