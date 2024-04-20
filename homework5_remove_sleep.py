from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.wait = WebDriverWait(driver, timeout=10)

driver.get('http://www.target.com/')

search = driver.find_element(By.NAME, 'searchTerm')
search.clear()
search.send_keys('lamp')

#wait for 4 sec
#driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK'))).click()

search_bt = (By.XPATH,"//button[@aria-label='search'][@type='submit']")
driver.wait.until(EC.element_to_be_clickable(search_bt), message='Search btn not clickable').click()
driver.wait.until(EC.title_contains("Lamp"))
print(driver.current_url.lower())

assert 'lamp' in driver.current_url.lower(), f"Expected query not in {driver.current_url_lower()}"
print('Test Passed')

driver.quit()







