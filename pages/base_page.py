

class Page:          #generic base page
    def __init__(self, driver):
        self.driver = driver


    def find_element(self, *locator):
        return self.driver.find_element(*locator)


    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)


    def click(self, *locator):
        self.find_element(*locator).click()


    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)


    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'



#      def verify_partial_text(self, expected_text, *locator):
#         actual_text = self.find_element(*locator).text
#         assert expected_text in actual_text , f'Expected {expected_text} not in {actual_text}'




















