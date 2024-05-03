from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


from app.application import Application

def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    #driver_path = GeckoDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Firefox(service=service)

    # BROWSERS WITH DRIVERS: provide path to the driver file ### not very using this function browser
    #service = Service(executable_path='C:\Users\Nandini\python-selenium-automation\operadriver_win32')
    #context.driver = webdriver.chrome(service=service)

    ### SAFARI ###
    # context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    #Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'nandinisarkar_SA5mDb'
    bs_key = 'RsMZ3Z1HxxvquWC5kV2q'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'


    options = Options()
    bstack_options = {
        'os': 'Window',
        'osVersion': '10',
        'browserName': 'chrome',
        'sessionName': 'User can open and close Terms and Conditions from sign in page'
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, timeout=15)

    context.app = Application(context.driver)    # excess to main_page, header, search_result_page

    #context.app.header
    #context.app.main_page

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        context.app.base_page.save_screenshot(step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()














