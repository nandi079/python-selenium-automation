from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service=Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com')
#driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
#sleep(5)
driver.find_element(By.XPATH,"//a[@data-nav-role='signin']").click()

#driver.find_element(By.ID,'twotabsearchtextbox')

if driver.find_element(By.XPATH,"//i[@aria-label='Amazon']"):
    print("Element Amazon Logo found")

if driver.find_element(By.XPATH,"//input[@id='ap_email']"):
    print("Element Email input field found")

if driver.find_element(By.XPATH,"//input[@id='continue' and @type='submit' and @aria-labelledby='continue-announce']"):
    print("Element continue button found")

if driver.find_element(By.XPATH,'//a[contains(@href,"ap_signin_notification_condition_of_use")]'):
    print("Found Conditions of Use link")

if driver.find_element(By.XPATH,'//a[contains(@href,"ap_signin_notification_privacy_notice")]'):
    print("Found Privacy Notice link")

if driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']"):
    print("Found Need Help")
    driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']").click()

#if driver.find_element(By.XPATH,'//a[contains(@href,"ap/forgotpassword?")]'):
 #   print("Found Forgot Password link")

if driver.find_element(By.XPATH,"//a[@id='auth-fpp-link-bottom']"):
    print("Found Forgot Password link")
    driver.find_element(By.XPATH,"//a[@id='auth-fpp-link-bottom']").click()
    sleep(5)
    driver.back()

driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']").click()

if driver.find_element(By.XPATH,"//a[@id='ap-other-signin-issues-link']"):
    print("Found Other issues with Sign-In link")
    driver.find_element(By.XPATH,"//a[@id='ap-other-signin-issues-link']").click()
    sleep(5)
    driver.back()

if driver.find_element(By.XPATH,"//a[@id='createAccountSubmit']"):
    print("Found Create Amazon Account link")
    driver.find_element(By.XPATH,"//a[@id='createAccountSubmit']").click()
    sleep(5)
    driver.back()

sleep(10)

print("Test Passed")

driver.quit()