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
driver.get('https://www.target.com')

#click sign in icon on top
driver.find_element(By.XPATH,"//a[@data-test='@web/AccountLink']").click()
sleep(2)

#click Sign in link on the sidebar
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(2)

#find Sign into you Target account text
actual_text = driver.find_element(By.XPATH,"//h1[@class='styles__StyledHeading-sc-1xmf98v-0 styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa']").text
#print(actual_text)
assert 'Sign into your Target account' in actual_text, f'Error!'
print('Test case Sign into your Target account text - passed')
#driver.find_element(By.XPATH,"//span[@class='Sign into your Target account']")
#sleep(10)

if driver.find_element(By.XPATH, "//button[@id='login']"):
        print('Test case found SignIn button - passed')