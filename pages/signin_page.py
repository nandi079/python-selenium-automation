from selenium.webdriver.common.by import By

from pages.base_page import Page
from time import sleep

class SignInPage(Page):
    SIGNIN_BUTTON = (By.XPATH, "//a[@aria-label='Account, sign in']")
    NAV_SIGNIN_BUTTON = (By.XPATH, "//a[@data-test='accountNav-signIn']")
    VERIFY_SIGNIN_HEADER = (By.CSS_SELECTOR, "h1[class*='styles__StyledHeading']")
    EMAIL_FIELD_NAME = (By.CSS_SELECTOR, "input[id='username']")
    PASSWORD_FIELD_NAME = (By.CSS_SELECTOR, "input[id='password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    VERIFY_LOGIN_NAME = (By.XPATH, "//a[@data-test='@web/AccountLink']")
    CLICK_LINK = (By.CSS_SELECTOR, "a[href='/c/terms-conditions/-/N-4sr7l']")

    def click_target_signin_button(self):
        self.click(*self.SIGNIN_BUTTON)

    def open_sign_in_page(self):
        self.click(*self.CLICK_LINK)

    def click_nav_signin_button(self):
        self.click(*self.NAV_SIGNIN_BUTTON)
        sleep(3)


    def verify_signin_page(self):
        self.verify_text('Sign into your Target account', *self.VERIFY_SIGNIN_HEADER)


    def input_field(self, text):
        self.input_text(text,*self.EMAIL_FIELD_NAME)

    def password_field(self,text):
        self.input_text(text, *self.PASSWORD_FIELD_NAME)
        sleep(1)

    def click_submit_login(self):
        self.click(*self.SUBMIT_BUTTON)
        sleep(5)

    def verify_user_loggedin(self,expected_name):
        self.verify_partial_text(expected_name, *self.VERIFY_LOGIN_NAME)
        sleep(3)


    def click_conditions_link(self):
        self.click(*self.CLICK_LINK)
        sleep(3)

    def verify_link_opened(self):       #create on another page object
        self.verify_url('/c/terms-conditions/')
        sleep(5)