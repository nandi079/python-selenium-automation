from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import Page
from time import sleep

class HelpPage(Page):
    HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    HEADER = (By.XPATH, "//h1[text()=' {HEADER_STR}']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    HEADER_PROMOTIONS_COUPONS = (By.XPATH, "//h1[text()=' Promotions & Coupons']")
    HEADER_PROMOTIONS = (By.XPATH, "//h1[text()=' Current promotions']")

    HEADER_TARGET_CIRCLE = (By.XPATH, "//h1[text()=' Target Circle™']")
    HEADER_ABOUT_TARGET_CIRCLE = (By.XPATH, "//h1[text()=' About Target Circle']")


    HEADER_GIFT_CARDS = (By.XPATH, "//h1[text()=' Gift Cards']")
    HEADER_GIFT_CARDS_BALANCE = (By.XPATH, "//h1[text()=' Target GiftCard balance']")


    def open_help_returns(self):
        self.open('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')
        sleep(4)

    def _get_locator(self, text):
        return [self.HEADER[0], self.HEADER[1].replace('{HEADER_STR}', text)]


    def select_topic(self, option):
        topic_dd = self.find_element(*self.TOPIC_SELECTION)
        select = Select(topic_dd)
        select.select_by_value('Gift Cards')
        sleep(4)


    def verify_header(self, header):
        locator = self._get_locator(header)
        self.wait_until_visible(*locator)


# _get_locator define all topic selections. Also, covered promotion and return header funtions.
   # def verify_returns_header(self):
    #     self.wait_until_visible(*self.HEADER_RETURNS)


    #def verify_promotions_header(self):
     #    self.wait_until_visible(*self.HEADER_PROMOTIONS)












