from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "div[class*='StyledHeaderWrapper'] color")
SELECTED_COLOR = (By.CSS_SELECTOR, "div[class*='styles__StyledVariationSelectorImage']")


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['dark khaki', 'black/gum', 'stone/grey', 'white/gum']
    actual_colors = []

@then('verify and select product colors')
def verify_and_select_product_colors(context):
    expected_colors = ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Current_color', selected_color)

        selected_color = selected_color.split('\n',1)[-1]
        actual_colors.append(selected_color)
        print('Actual --',actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'




