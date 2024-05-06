from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Page:          #generic base page
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)


    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)


    def click(self, *locator):
        self.find_element(*locator).click()


    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def wait_until_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            f'Element not clickable by {locator}'
        ).click()

    def wait_until_visible(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            f'Element not visible by {locator}'
        )

    def wait_until_disappears(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            f'Element still visible by {locator}'
        )



    def get_current_window(self):
        current_window = self.driver.current_window_handle
        print('current:', current_window)
        print('ALL windows:', self.driver.window_handles)
        return current_window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles  #window1,2,3..
        print('ALL windows:', self.driver.window_handles)
        print('switching to ...', all_windows[1])   # use index [0] to return to first window
        self.driver.switch_to.window(all_windows[1])


    def switch_window_by_id(self, window_id):
        print('Switching to... ', window_id)
        self.driver.switch_to.window(window_id)


    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'


    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} not in {actual_text}'


    def verify_url(self, expected_url):
        self.wait.until(EC.url_matches(expected_url),f'Url does not contain {expected_url}')


    def save_screenshot(self, name):
        self.driver.save_screenshot(f'{name}.png')


    def close(self):
        self.driver.close()

















