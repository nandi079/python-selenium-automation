from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Amazon signin page')
def open_Amazon_page(context):
    context.driver.get('https://www.amazon.com')
    sleep(4)
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='signin']").click()
    context.driver.find_element(By.CSS_SELECTOR, "#auth-create-account-link").click()

@when('Fill the user details form')
def fill_form(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='/ref=ap_frn_logo']")
    context.driver.find_element(By.CSS_SELECTOR, "h1[class*='a-spacing-small']")
    context.driver.find_element(By.CSS_SELECTOR, "h1[class*='a-spacing-small']")
    context.driver.find_element(By.CSS_SELECTOR, "input[placeholder='First and last name']")
    sleep(3)

    context.driver.find_element(By.CSS_SELECTOR, "input#ap_email")
    context.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    context.driver.find_element(By.CSS_SELECTOR, "div[class*='a-alert-content']")
    context.driver.find_element(By.CSS_SELECTOR, "input[name='passwordCheck']")
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "input[id='continue'][type='submit'][aria-labelledby='auth-continue-announce']")

@then('Account policy details')
def Account_policy(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='ap_altreg_ab']")
    context.driver.find_element(By.CSS_SELECTOR, "a[class*='a-link-emphasis']")