from behave import when, then


@then('Click on Target Signin button')
def target_signin_button(context):
    context.app.signin_page.click_target_signin_button()


@then('Click on Signin button on right side navigation')
def click_nav_signin_button(context):
    context.app.signin_page.click_nav_signin_button()


@then('Verify Signin page opened')
def verify_signin_page(context):
    context.app.signin_page.verify_signin_page()


@then('Input field {expected_field} is entered')
def input_field(context,expected_field):
    context.app.signin_page.input_field(expected_field)


@then('Input password field {expected_field} is entered')
def password_field(context,expected_field):
    context.app.signin_page.password_field(expected_field)


@then('click on submit button')
def submit_login(context):
    context.app.signin_page.click_submit_login()


@then('Verifies {expected_text} message is shown')
def verify_account(context,expected_text):
    context.app.signin_page.verify_account(expected_text)





@then('Verify {expected_name} is logged in target page')
def verify_user(context,expected_name):
    context.app.signin_page.verify_user_loggedin(expected_name)


@when('store original window')
def store_original_window(context):
    context.original_window = context.app.signin_page.get_current_window()


@when('Click on Target terms and conditions link')
def click_conditions_link(context):
    context.app.signin_page.click_conditions_link()

@when('Switch to the newly opened window')
def switch_window(context):
    context.app.signin_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_link_opened(context):
    context.app.signin_page.verify_link_opened()


@then('User can close new window')
def close(context):
    context.app.signin_page.close()


@then('Switch back to original')
def return_to_original_window(context):
    context.app.signin_page.switch_window_by_id(context.original_window)



