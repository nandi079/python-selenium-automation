from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SearchResultsPage(Page):
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")

    def search_results(self, expected_item):
        actual_text = self.find_element(*self.SEARCH_RESULT_HEADER).text
        print(actual_text)
        sleep(5)
        assert expected_item in actual_text, f'Error! text {expected_item} not in {actual_text}'






