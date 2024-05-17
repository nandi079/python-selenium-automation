from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    SIGNIN_BUTTON = (By.XPATH, "//a[@aria-label='Account, sign in']")
    NAV_SIGNIN_BUTTON = (By.XPATH, "//a[@data-test='accountNav-signIn']")
    VERIFY_SIGNIN_HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")

    def click_target_signin_button(self):
        self.click(*self.SIGNIN_BUTTON)


    def click_nav_signin_button(self):
        self.click(*self.NAV_SIGNIN_BUTTON)


    def verify_signin_page(self):
        self.verify_text('Sign into your Target account', *self.VERIFY_SIGNIN_HEADER)
