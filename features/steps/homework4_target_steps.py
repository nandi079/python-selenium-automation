from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.ID,'links')
SEARCH_BIN=(By.XPATH, "class*='styles__StyledLink']")
LINKS = (By.CSS_SELECTOR, "a[data-test*='@web/slingshot-components/CellsComponent/Link']")

@given('Open Target Circle page')
def open_target_circle_page(context):
    context.driver.get('http://www.target.com/circle')

@when('Click on search bar')
def click_search_bar(context):
    context.driver.find_element(By.CSS_SELECTOR, "input[data-test='@web/Search/SearchInput']")
    sleep(3)




@when('Select Target circle')
def target_circle(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/circle']").click()
    sleep(3)

@then('Verify {count} links present')
def verify_links(context,count):
    links = context.driver.find_elements(*LINKS)
    #print(links)
    assert len(links) == count, f'Expected {count} links found {len(links)}'


@then('Add to cart')
def add_to_cart(context):
    sleep(5)
    context.driver.find_element(By.XPATH,"//*[@id='addToCartButtonOrTextIdFor47966546']").click()
    sleep(5)
    context.driver.find_element(By.XPATH,"//*[@data-test='shippingButton' and @id='addToCartButtonOrTextIdFor47966546']").click()
    sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/cart']").click()
    sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, "[class*='styles__CartSummarySpan']")
    sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label='Target home']").click()
    sleep(3)

    #End Homework 4 steps