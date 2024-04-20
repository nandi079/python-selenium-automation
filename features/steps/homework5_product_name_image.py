from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then
from time import sleep


SEARCH_INPUT = (By.ID,'search')
SEARCH_BTN = (By.XPATH, "[data-test='@web/Search/SearchInput']")
#LISTINGS = (By.CSS_SELECTOR, "[class*='styles__ProductCardItemInfoDiv'][class*='styles__StyledProductCardImageWrapper']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")

@given('Open target start page')
def open_target(context):
    context.driver.get('https://www.target.com')
    sleep(1)

@when("Searching 'coffee'")
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('coffee')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(1)

@then('Verify Product Title and Image is shown')
def verify_product_present(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(2)
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(2)
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(2)
    #context.driver.execute_script("window.scrollBy(0,2000)", "")
    #sleep(2)

    all_products = context.driver.find_elements(*LISTINGS)
    print('List of items',len(all_products))
    count=1

    for product in all_products:

        title = product.find_element(*PRODUCT_TITLE).text
        #sleep(1)
        print(count, title)
        count=count+1
        assert title, 'Product title not shown'
        product.find_element(*PRODUCT_IMG)





