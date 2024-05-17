from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.amazon.com")  # open the URl

driver.find_element(By.ID,'twotabsearchtextbox')   #by IDs
driver.find_element(By.ID, 'navFooter')

driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")  #by XPATH

driver.find_element(By.XPATH, "//input[@type='text' and @name= 'field-keywords']")   # multi attribute

driver.find_element(By.XPATH, "//a[text()='Best Sellers']")  # By text

driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")  # by text and attribute
driver.find_element(By.XPATH, "//a[class='nav-a  ' and text()='Best Sellers']")