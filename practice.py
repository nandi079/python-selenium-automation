from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service=Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#open website
driver.get('https://www.amazon.com')

driver.find_element(By.ID, "nav-link-accountList").click()

#click sign in icon on top
driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys('2404690762')
sleep(2)

driver.find_element(By.XPATH, "//input[@id='continue']").click()
sleep(2)

driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys('yellowjacket79')
sleep(2)

driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()
sleep(2)

# verification
actual_text = driver.find_element(By.XPATH,"//span[@id='nav-link-accountList-nav-line-1']").text
print(actual_text)
assert 'nandini' in actual_text, f'Error! password is {actual_text}'
print('Test case passed')

#driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()
driver.quit()


